# GitHub Actions Modifications

Modify the GitHub Actions workflow defined in the [run_tests.yml](/.github/workflows/run_tests.yml) file as follows:

1. For the **Install dependencies** step:

    ```yaml
    - name: Install dependencies
      run: 
     ```
     
     update the **run** command as follows:

    ```yaml
    - name: Install dependencies
      run: pip install -r requirements.txt
    ```

2. For the **Run tests** step:

    ```yaml
    - name: Run tests
      run: 
     ```
     
     update the **run** command as follows:

    ```yaml
    - name: Run tests
      run: python -m unittest discover tests/
    ```
