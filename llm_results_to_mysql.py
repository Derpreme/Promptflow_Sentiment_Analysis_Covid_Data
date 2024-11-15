from promptflow.core import tool
import mysql.connector
from mysql.connector import Error
import json

@tool(input_schema={"data": "string"}, output_schema={"update_status": "string"})
def update_llm_sentiment_labels(data):

    # Connection details
    host = 'wix-mysql-server-name.mysql.database.azure.com'
    database = 'mysqltutorial'
    user = 'shuzhennong'  # Your Azure MySQL username
    password = 'Fudan@0216$'  # Your Azure MySQL password

    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Connection established successfully.")

        # Create a cursor object using the connection
        cursor = connection.cursor()
        
        input_dict = json.loads(data)
        # Check if input_dict is actually a dictionary and contains the 'data' key
        if isinstance(input_dict, dict) and "data" in input_dict:
            # If input_dict is a dictionary and has a 'data' key, parse the JSON string from 'data' key
            data_list = json.loads(input_dict["data"])
        elif isinstance(input_dict, list):
            # If input_dict is directly a list, use it as is
            data_list = input_dict
        else:
            # Handle unexpected data structure
            raise ValueError("Unexpected data structure received.")

        # Proceed with processing data_list as before
           
        if not isinstance(data_list, list):
            return {"update_status": "Failed due to incorrect data format: data is not a list"}

        # Update each row with the new LLM_Sentiment_Label
        for item in data_list:
            # Ensure each item is a dictionary
            if not isinstance(item, dict):
                print("Skipping item due to incorrect format: item is not a dictionary")
                continue

            sentence_id = item.get('Sentence_ID')
            llm_sentiment_label = item.get('LLM_Sentiment_Label')
            if sentence_id is None or llm_sentiment_label is None:
                print("Skipping item due to missing Sentence_ID or LLM_Sentiment_Label")
                continue

            query = """UPDATE mysqltutorial.Covid_Data_For_Sentiment_Analysis
                       SET LLM_Sentiment_Label_GPT4o = %s
                       WHERE Sentence_ID = %s;"""
            cursor.execute(query, (llm_sentiment_label, sentence_id))
        
        connection.commit()
        print(f"Updated {len(data)} rows with LLM sentiment labels.")

    except Error as ex:
        error_message = ex.msg
        print(f"Error message: {error_message}")
        return {"update_status": "Failed due to error: " + error_message}
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")
    
    return {"update_status": "Success"}

# Example usage
if __name__ == "__main__":
    input_str = """
    {
      "data": "[{\\n    \\"Sentence_ID\\": \\"1\\",\\n    \\"LLM_Sentiment_Label\\": \\"-1\\"\\n  },  \\n  {\\n    \\"Sentence_ID\\": \\"2\\",\\n    \\"LLM_Sentiment_Label\\": \\"-1\\"\\n  },  \\n  {\\n    \\"Sentence_ID\\": \\"3\\",\\n    \\"LLM_Sentiment_Label\\": \\"-1\\"\\n  },  \\n  {\\n    \\"Sentence_ID\\": \\"4\\",\\n    \\"LLM_Sentiment_Label\\": \\"0\\"\\n  },  \\n  {\\n    \\"Sentence_ID\\": \\"5\\",\\n    \\"LLM_Sentiment_Label\\": \\"0\\"\\n  },  \\n  {\\n    \\"Sentence_ID\\": \\"6\\",\\n    \\"LLM_Sentiment_Label\\": \\"-1\\"\\n  },  \\n  {\\n    \\"Sentence_ID\\": \\"7\\",\\n    \\"LLM_Sentiment_Label\\": \\"-1\\"\\n  },  \\n  {\\n    \\"Sentence_ID\\": \\"8\\",\\n    \\"LLM_Sentiment_Label\\": \\"-1\\"\\n  },  \\n  {\\n    \\"Sentence_ID\\": \\"9\\",\\n    \\"LLM_Sentiment_Label\\": \\"0\\"\\n  },  \\n  {\\n    \\"Sentence_ID\\": \\"10\\",\\n    \\"LLM_Sentiment_Label\\": \\"-1\\"\\n  }\\n]"
    }
    """
    
    # Now, data is the actual list of dictionaries
    output = update_llm_sentiment_labels(input_str)
    print(output)