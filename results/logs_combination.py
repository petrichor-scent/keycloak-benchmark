import os

def list_subdirectories(directory):
    subdirectories = []
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            subdirectories.append(item)
    return subdirectories

def concatenate_text_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for filename in input_files:
            with open(filename, 'r') as infile:
                outfile.write(infile.read())

if __name__=="__main__":
    directory_path = "/home/lamle/CMP/keycloak-benchmark-0.9-SNAPSHOT/results"
    subdirectories = list_subdirectories(directory_path)
    simulation_logs = [("./"+item+"/simulation.log") for item in subdirectories]

    for log in simulation_logs:
        print(log)
    concatenate_text_files(simulation_logs, "./simulation.log")
