from flask import Flask, request, jsonify
import subprocess
from nlp_module import extract_parameters
from retriver import retrieve_best_match
from generator import generate_response

app = Flask(__name__)

@app.route('/configure_ran', methods=['POST'])
def configure_ran():
    data = request.json
    params = extract_parameters(data.get('message'))
    
    if not params["frequency"] or not params["bandwidth"]:
        return jsonify({"status": "error", "message": "Invalid input. Please specify frequency and bandwidth."})

    retrieved_info = retrieve_best_match(data.get('message'))
    
    prompt = f"Generate a configuration file for RAN with frequency {params['frequency']} MHz and bandwidth {params['bandwidth']} MHz using: {retrieved_info}"
    config_instructions = generate_response(prompt)
    
    # Save configuration to gnb.conf
    with open("gnb.conf", "w") as config_file:
        config_file.write(config_instructions)

    # Apply the configuration by restarting the gNB
    subprocess.run(["sudo", "./cmake_targets/ran_build/build/gnb", "-c", "./gnb.conf"])
    
    return jsonify({"status": "Success", "details": config_instructions})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
