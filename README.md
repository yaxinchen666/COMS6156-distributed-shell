# Grader with distributed shell (pssh & dish)

This repo contains the code for an auto-grader with two distributed shells.

Our tool (`/pssh/grading.py` and `/dish/grading.py`) reads a config file in json format specifying:

**host_file** (required): path to the file storing `username@ip` of students' machines (need to set up ssh connection from instructor's machine to students' machines beforehand)

**time_out**: connection time out in seconds

**local_file**: local file/directory to be copied to students' machines

**destination**: destination path on students' machines to store `local_file`

**grading_script**: path to the grading script on students' machines

**grading_dir**: working directory when running the grading script

**pre_commands**: bash commands to be executed before running the grading script

**post_commands**: bash commands to be executed after running the grading script

**result_path**: path on the instructor's machine to put the execution results of grading

## Repository Structure

`/project_assignments`: all project assignments

`/pssh`: grading tool built with pssh

`/dish`: grading tool built with dish

`/test`: testing files for comparison of pssh and dish.

## Run the tool

### pssh examples

Example config files and grading script are under `pssh/hw1_setup_files` and `pssh/hw1_grading_files`.

Before running, make sure the instructor's machine can access all student machines via ssh and modify `pssh/host_file` to include usernames and ip addresses of student machines. Install pssh and pscp by:

```bash
sudo apt-get install pssh
sudo apt-get install pscp
```

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


### dish examples

Example config files and grading script are under `dish/config.json` and `dish/hw1_grader.py`.

To install dish, run the following commands: 

```bash
sudo apt-get install dish
```

Clone the repository.  Fill out the ```host_file``` with the usernames and IPs of student machines. 

```bash
cd dish
python3 grading.py config.json
cat hw1_grading_result
```



