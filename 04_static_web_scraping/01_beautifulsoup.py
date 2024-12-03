from bs4 import BeautifulSoup as bs, Comment
import json

"""
Complete each of the functions below by filling in the missing code.
Follow the TODO instructions carefully to extract the required data.
"""

def extract_attributes() -> str:
    """
    Extract the 'data-id' attribute from the <img> tag in the HTML.
    Return the value of the 'data-id' attribute as a string.
    """
    html = """
        <img src="image1.jpg" alt="A beautiful landscape" data-id="12345">
        """
    soup = bs(html, "html.parser")
    
    # TODO: Locate the <img> tag
    img = None  # Replace None with the appropriate BeautifulSoup method.
    
    # TODO: Extract the 'data-id' attribute from the <img> tag
    return None  # Replace None with the extracted value.


def extract_tables() -> list[dict]:
    """
    Extract data from an HTML table and return it as a list of dictionaries.
    Each dictionary should represent a row, with keys as column headers and values as row data.
    Example Output:
    [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
    """
    html = """
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Alice</td>
                <td>30</td>
            </tr>
            <tr>
                <td>Bob</td>
                <td>25</td>
            </tr>
        </tbody>
    </table>
    """
    soup = bs(html, "html.parser")
    
    # TODO: Find all rows of data inside the <tbody> tag
    rows = None  # Replace None with the appropriate method to find rows.

    # TODO: Define the headers based on the <thead> (e.g., ["name", "age"])
    headers = None  # Replace None with a list of column headers.

    result = []
    # TODO: Iterate through each row and extract data into a dictionary
    for row in rows:
        # Extract <td> elements from the row
        cells = None  # Replace None with the method to find all <td> elements in the row.
        # Extract text from cells and map to headers
        data = None  # Replace None with a list of cell text.
        # Create a dictionary and append to the result list
        result.append(None)  # Replace None with a dictionary using zip(headers, data).

    return result


def extract_scripts() -> dict:
    """
    Extract JSON-like data embedded in a <script> tag.
    Return the parsed JSON data as a Python dictionary.
    Example Output:
    {"id": 123, "name": "Alice"}
    """
    html = """
        <script>
            var userInfo = { "id": 123, "name": "Alice" };
        </script>
        """
    soup = bs(html, "html.parser")
    
    # TODO: Locate the <script> tag and extract its content
    script_content = None  # Replace None with the script content.

    # TODO: Clean the script content to isolate the JSON structure
    json_text = None  # Replace None with cleaned text to extract JSON.

    # TODO: Parse the JSON text and return as a dictionary
    return None  # Replace None with the parsed JSON.


def extract_comments() -> str:
    """
    Extract a comment embedded in the HTML.
    Return the comment as a string.
    Example Output:
    ' User ID: 67890 '
    """
    html = """
        <!-- User ID: 67890 -->
        <div class="user-info">Name: John Doe</div>
        """
    soup = bs(html, "html.parser")
    
    # TODO: Find the comment in the HTML using BeautifulSoup's Comment filter
    comment = None  # Replace None with the comment content.
    return comment


def extract_dynamic_classes() -> list[str]:
    """
    Extract text content from all <div> elements with class names starting with 'content-'.
    Return the extracted text content as a list of strings.
    Example Output:
    ['Item 1', 'Item 2', 'Item 3']
    """
    html = """
        <div class="content-1">Item 1</div>
        <div class="content-2">Item 2</div>
        <div class="content-3">Item 3</div>
        """
    soup = bs(html, "html.parser")
    
    # TODO: Find all <div> elements with class names starting with "content-"
    divs = None  # Replace None with the appropriate method to find the elements.

    # TODO: Extract the text content from each <div> and return as a list
    return None  # Replace None with a list of text from each <div>.


""" 
Do not modify the code below. It handles test cases for your functions.
Complete all functions above and run the tests to verify correctness.
"""

def assessment(expected_result, actual_result):
    """
    Compare the expected result with the actual result from a function.
    Return True if they match, otherwise False.
    """
    return expected_result == actual_result

def run_tests():
    """
    Run predefined test cases to validate each function.
    Print feedback and the total score.
    """
    test_cases = [
        {
            "label": "Extract Attributes",
            "expected_result": "12345",
            "func": extract_attributes
        },
        {
            "label": "Extract Tables",
            "expected_result": [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}],
            "func": extract_tables
        },
        {
            "label": "Extract Scripts",
            "expected_result": {"id": 123, "name": "Alice"},
            "func": extract_scripts
        },
        {
            "label": "Extract Comments",
            "expected_result": ' User ID: 67890 ',
            "func": extract_comments
        },
        {
            "label": "Extract Dynamic Classes",
            "expected_result": ['Item 1', 'Item 2', 'Item 3'],
            "func": extract_dynamic_classes
        },
    ]

    score = 0
    total_tests = len(test_cases)

    for test in test_cases:
        # Run the test function and compare the result
        if assessment(test["expected_result"], test["func"]()):
            score += 1
            print(f"{test['label']} - Correct!")
        else:
            print(f"{test['label']} - Incorrect. Expected {test['expected_result']}.")

    # Calculate and print the final score
    print(f"Total score: {score / total_tests * 100}%")

if __name__ == "__main__":
    run_tests()
