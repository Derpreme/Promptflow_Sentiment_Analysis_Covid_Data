from promptflow.core import tool
import mysql.connector
from mysql.connector import Error

@tool(input_schema={"dummy_input": "string"}, output_schema={"sentences": "list", "update_status": "string"})
def fetch_sentences(dummy_input):
    try:
        connection = mysql.connector.connect(
            host='wix-mysql-server-name.mysql.database.azure.com',
            database='mysqltutorial',
            user='shuzhennong',
            password='Fudan@0216$'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT Sentence_ID, Sentence FROM mysqltutorial.Covid_Data_For_Sentiment_Analysis WHERE Sentence_ID >= 976 AND Sentence_ID <= 1000;")
            records = cursor.fetchall()
            return {"sentences": records, "update_status": "Success"}
    except Error as e:
        print("Error while connecting to MySQL", e)
        return {"sentences": [], "update_status": f"Failed due to error: {e}"}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    dummy_data = {"dummy_input": "none"}  # Dummy input
    sentences = fetch_sentences(dummy_data)
    print(sentences)