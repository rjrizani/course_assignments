import json

from bs4 import BeautifulSoup as bs, Comment


"""
Complete all of the functions below
to extract data from the HTML.
"""

def extract_attributes()->str:
    """
    Extract the attribute data into a string
    """
    
    html = """
        <img src="image1.jpg" alt="A beautiful landscape" data-id="12345">
        """
    
    # Your code here


def extract_tables()->list[dict]:
    """
    Extract the table data into a list of dictionaries
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

    # Your code here


def extract_scripts()->dict:
    """
    Extract the script data into a dictionary
    """

    html = """
        <script>
            var userInfo = { "id": 123, "name": "Alice" };
        </script>
        """

    # Your code here


def extract_comments()->str:
    """
    Extract the comment data into a string
    """

    html = """
        <!-- User ID: 67890 -->
        <div class="user-info">Name: John Doe</div>
        """
    
    # Your code here


def extract_dynamic_classes()->list[str]:
    """
    Extract the dynamic class data into a list of strings
    """

    html = """
        <div class="content-1">Item 1</div>
        <div class="content-2">Item 2</div>
        <div class="content-3">Item 3</div>
        """

    # Your code here



""" Dont change the code below """

def assessment(expected_result, actual_result):
    return expected_result == actual_result

def run_tests():
    # List of test cases with their expected results and the function to call
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
        # Add more test cases as needed
        # {
        #     "label": "Test Case 2",
        #     "expected_result": expected_result_2,
        #     "func": extract_items,
        # },
    ]

    score = 0
    total_tests = len(test_cases)

    for test in test_cases:
        # Run the test and check the result
        if assessment(test["expected_result"], test["func"]()):
            score += 1
            print(f"{test['label']} - Correct!")
        else:
            print(f"{test['label']} - Try again!")

    # Calculate and print the score
    print(f"Total score: {score / total_tests * 100}%")

if __name__ == "__main__":
    run_tests()

