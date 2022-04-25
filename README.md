# Grader with distributed shell (pssh & dish)

`grading.py` takes a config file in json format specifying:

**host_file** (required): path to the file storing `username@ip` of students' machines (need to set up ssh connection from instructor's machine to students' machines beforehand)

**time_out**: connection time out in seconds

**local_file**: local file/directory to be copied to students' machines

**destination**: destination path on students' machines to store `local_file`

**grading_script**: path to the grading script on students' machines

**grading_dir**: working directory when running the grading script

**pre_commands**: bash commands to be executed before running the grading script

**post_commands**: bash commands to be executed after running the grading script

**result_path**: path on the instructor's machine to put the execution results of grading

### pssh examples

Example config files and grading script are under `pssh/hw1_setup_files` and `pssh/hw1_grading_files`.

To set up hw1 (copy starter code to students' machines):

```bash
cd pssh/hw1_setup_files
python ../grading.py hw1_setup_config.json
```

To grade hw1 (copy `hw1_grading` to students' machines, run `hw1_grading.sh` and collect result):

```bash
cd pssh/hw1_grading_files
python ../grading.py hw1_grading_config.json
cat hw1_grading_result
```

