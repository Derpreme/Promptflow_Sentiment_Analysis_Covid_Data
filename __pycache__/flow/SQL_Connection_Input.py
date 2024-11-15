from promptflow.core import tool
import pyodbc

@tool(input_schema={"query": "string"}, output_schema={"results": "string"})
def fetch_data_from_mssql(query):
    # Connection details
    server = 'tcp:studentvoice-server.database.windows.net,1433'
    database = 'Survey_Database'
    username = 'ShuzhenNong@DreamJobcom.onmicrosoft.com'  # Replace with your Microsoft Entra username
    password = 'Fudan@0216$'  # Replace with your Microsoft Entra password

    # Connection string
    connection_string = (
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=' + server + ';'
        'DATABASE=' + database + ';'
        'UID=' + username + ';'
        'PWD=' + password + ';'
        'Encrypt=yes;'
        'TrustServerCertificate=no;'
        'Connection Timeout=60;'  # Increased timeout
        'Authentication=ActiveDirectoryPassword'
    )

    results = ''
    
    try:
        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)
        print("Connection established successfully.")

        # Create a cursor object using the connection
        cursor = connection.cursor()

        # Execute the query
        print(f"Executing query: {query}")
        cursor.execute(query)

        # Fetch the results
        rows = cursor.fetchall()
        print(f"Number of rows fetched: {len(rows)}")

        # Concatenate the results into a single string
        results = ', '.join([str(row[0]) for row in rows])

    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        error_message = ex.args[1]
        print(f"SQLSTATE: {sqlstate}")
        print(f"Error message: {error_message}")
    finally:
        # Close the connection
        if 'connection' in locals():
            connection.close()
            print("Connection closed.")
    
    print(f"Results: {results}")
    return {"results": results}

# Example usage
if __name__ == "__main__":
    query = 'SELECT Question3 FROM dbo.survey1;'
    output = fetch_data_from_mssql(query)
    print(output)
