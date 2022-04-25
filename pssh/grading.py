import os
import json
import sys

HOST_FILE_STR = "host_file"
LOCAL_FILE_STR = "local_file"
DESTINATION_STR = "destination"
GRADING_SCRIPT_STR = "grading_script"
GRADING_DIR_STR = "grading_dir"
GRADING_COMMAND_STR = "grading_command"
PRE_COMMANDS_STR = "pre_commands"
POST_COMMANDS_STR = "post_commands"
RESULT_PATH_STR = "result_path"

def read_config(file_path):
  if not os.path.exists(file_path):
    sys.exit("Error: no such file: '" + file_path + "'")
  f = open(file_path)
  config = json.load(f)
  return config


def grading(config):
  if HOST_FILE_STR not in config:
    sys.exit("Error: lack host_file in config")

  # copy local files to destination
  if LOCAL_FILE_STR in config and DESTINATION_STR in config:
    print("Copying local file to student machines...")
    local_file = config[LOCAL_FILE_STR]
    scp_str = ""
    if os.path.isfile(local_file):
      scp_str = "parallel-scp -v -h {} {} {}"
    elif os.path.isdir(local_file):
      scp_str = "parallel-scp -v -r -h {} {} {}"
    else:
      sys.exit("Error: no such file or directory: '" + local_file + "'")
    ret = os.system(scp_str.format(
      config[HOST_FILE_STR],
      config[LOCAL_FILE_STR],
      config[DESTINATION_STR]))
    if ret != 0:
      sys.exit("Fail to copy file {} to {}".format(config[LOCAL_FILE_STR], config[DESTINATION_STR]))

  # executing pre_commands
  if PRE_COMMANDS_STR in config:
    print("Executing " + PRE_COMMANDS_STR + "...")
    for command in config[PRE_COMMANDS_STR]:
      ret = os.system("parallel-ssh -h {} '{}'".format(config[HOST_FILE_STR], command))
      if ret != 0:
        print("Fail to execute '{}'".format(command))

  # grading
  if GRADING_COMMAND_STR in config or GRADING_SCRIPT_STR in config:
    print("Grading...")
    output_redirect = ""
    if RESULT_PATH_STR in config:
      output_redirect = " > " + config[RESULT_PATH_STR]

    cd_grading_dir = ""
    if GRADING_DIR_STR in config:
      cd_grading_dir = "cd " + config[GRADING_DIR_STR] + "; "

    command = ""
    if GRADING_COMMAND_STR in config:
      command = config[GRADING_COMMAND_STR]
    elif GRADING_SCRIPT_STR in config:
      filename, file_extension = os.path.splitext(config[GRADING_SCRIPT_STR])
      if file_extension == ".sh":
        command = "bash " + config[GRADING_SCRIPT_STR]
      elif file_extension == ".py":
        command = "python " + config[GRADING_SCRIPT_STR]
      else:
        print("Fail to run {}; should be .sh or .py".format(config[GRADING_SCRIPT_STR]))
    ret = os.system("parallel-ssh -i -h {} '{}' {}".format(
      config[HOST_FILE_STR],
      cd_grading_dir + command,
      output_redirect))
    if ret != 0:
      print("Fail to execute '{}'".format(command))

  # executing post_commands
  if POST_COMMANDS_STR in config:
    print("Executing " + POST_COMMANDS_STR + "...")
    for command in config[POST_COMMANDS_STR]:
      ret = os.system("parallel-ssh -h {} '{}'".format(config[HOST_FILE_STR], command))
      if ret != 0:
        print("Fail to execute '{}'".format(command))   

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    sys.exit("Error: lack config file")
  config = read_config(sys.argv[1])
  grading(config)
