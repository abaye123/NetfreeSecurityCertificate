import subprocess

def set_requests_ca_bundle():
    command = 'setx REQUESTS_CA_BUNDLE "%ProgramData%\\NetFree\\CA\\netfree-ca-bundle-curl.crt" -m'
    try:
        subprocess.run(command, shell=True, check=True)
        print("REQUESTS_CA_BUNDLE environment variable set successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting REQUESTS_CA_BUNDLE: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to set the environment variable
set_requests_ca_bundle()
