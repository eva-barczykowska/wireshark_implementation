# endpoint for the button to launch Wireshark

# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.post("/launch-wireshark")
# async def launch_wireshark():
#     # Call the Wireshark launch function using the subprocess module in Python.
#     import subprocess
#     subprocess.run(["wireshark"])
#     return {"message": "Wireshark launched successfully!"}


# run  uvicorn app:app --reload      to start the server

# version 2 with opening a specific profile:
from fastapi import FastAPI

app = FastAPI()


@app.api_route("/launch-wireshark", methods=["GET", "POST"])
async def launch_wireshark():
    import subprocess
    profile_name = "Wireshark Masterclass"  # Use your exact profile name here
    try:
        subprocess.run(["wireshark", "-C", profile_name], check=True)
        return {"message": f"Wireshark launched successfully with profile '{profile_name}'!"}
    except FileNotFoundError:
        return {"error": "Wireshark executable not found. Make sure it is installed and in your PATH."}
    except subprocess.CalledProcessError as e:
        return {"error": f"Wireshark failed to launch: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

