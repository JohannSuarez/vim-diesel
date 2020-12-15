# ______________________
# Author: Matt Williams |
# ----------------------

# Robust Makefile wrapper around pytest, because pytest doesnt do
# everything I want it to do I want customized functionality.
# This Makefile can be easily extended as the project gets larger
# to help us customize automated builds, testing, and other utility tasks
# The GNU make manual is a must read for any serious Linux user/hacker/programmer.
# it also just happens to be a fantastic read.
# https://www.gnu.org/software/make/manual

include ../config.mk


# ARGUMENT VARS
#=============#
# expression to search a test file for [eg] name of class
name ?= ""
# pass specific directory name
dir ?= ""

# DIRECTORY AND FILE VARS
# ==============
LOG_DIR      := pytest_logs/
RUNNER_FILE  := $(USER)_runner.py

# Use the C preprocessor to define blocks of POSIX shell code
# so we can avoid auto expansion, and having to escape every
# single piece of shell code syntax.
# These are also known as 'canned recipes' in the Makefile world.
# They aren't real functions, but more like old-school Fortran procedures.
# They cannot take in variables like f(x) , however we can define Make global
# variables that are initialized to empty strings, and use POSIX shell to treat
# them like parameters to functions.
# This also means I won't have to clutter the Library with make helper
# scripts, yet we can have a very powerful Makefile.

# standard help procedure
define help_show =
	$(_test_env)
	clear
	cat << EOF
	[                        The $(PKG_NAME) taskrunner                        ]

	Command         |                 Description                  |      Usage
	================|==============================================|===================
	help            |    Show this message                         |    make help
	debug-print     |    Print out all variable values             |    make debug-print
	all-tests       |    Run all tests, can take dir as arg        |    make all-tests or make all-tests dir=unit
	marked-tests    |    Run only tests that are marked            |    make marked-tests name=smoke
	log-tests       |    Drop all tests to pytest_logs/ folder     |    make log-tests
	filter-tests    |    Run specific test on specific function    |    make filter-tests name=test_config_loc
	run             |    generate or run manual test file          |    make run
	clean           |    remove any generated files or directories |    make clean
	
	EOF
endef


# Procedure for basic tests, if exp is empty, it will run all tests
# else it will run the tests with the specified directory as arg
define all_tests =
	$(_test_env)
	if [ -z $(dir) ]; then
		$(PY_TEST) $(PEDANTIC)
	else
		$(PY_TEST) $(PEDANTIC) $(dir)
	fi
endef

# Run only tests that are marked with pytest decorator
define marked_tests =
	$(_test_env)
	printf "$(BYellow)marked-tests: Not implemented yet$(Reset)\n"
endef


# Procedure to create and store pytest output into log files
# for grepping and other epic stuff
define log_tests =
	$(_test_env)
	[ ! -d $(LOG_DIR) ] && mkdir $(LOG_DIR) && printf "$(BGreen)Created $(LOG_DIR)$(Reset) ...\n"
	time_stamp=`date +"%F-%R"`
	file="pytest_log-"$$time_stamp".log"
	printf "$(BPurple)Running all tests$(Reset) ...\n"
	$(PY_TEST) $(PEDANTIC) > $(LOG_DIR)$$file
	[ $$? -eq 0 ] && printf "$(BGreen)All tests passed$(Reset) ...\n"
	printf "$(BGreen)Created "$$file" in $(LOG_DIR) directory$(Reset) ...\n"
endef


# Procedure to filter tests by function or method name, also show reason if reason is given
define filter_tests =
	$(_test_env)
	# make sure name var isn't empty
	[ -z $(name) ] && printf "$(BYellow)Requries argument,$(Reset) $(BWhite)[E.G]$(Reset): $(BBlue)make filter name=test_some_func$(Reset)\n" && exit 1

	$(PY_TEST) $(PEDANTIC) $(FILTER) "$(name)" $(REASON) "$(name)"
endef


# This is to run the runner.py file, which is not meant for pytest,
# this file is meant to make it easy for the programmer to write
# good ol manual test code
define run_runner =
	$(_test_env)
	cwd=`pwd`
	base=`basename $$cwd`
	
	# if the file exists execute it
	[ $$base = "tests" ] && [ -f $(RUNNER_FILE) ] && $(PY_INTERP) $(RUNNER_FILE)
	
	# if the file does not exist, then create it
	[ $$base = "tests" ] && [ ! -f $(RUNNER_FILE) ] && echo "# Write test code in here" >> $(RUNNER_FILE) && echo "$(BGreen)Created $(RUNNER_FILE)$(Reset)"
	
	# clear bad exit code with printf
	printf ""
endef


# clean up any generated files or directories
define clean_gen =
	$(_test_env)
	[ -f $(RUNNER_FILE) ] && rm $(RUNNER_FILE) && printf "$(BGreen)Removed $(RUNNER_FILE)$(Reset)\n"
	[ -d $(LOG_DIR) ] && rm -rf $(LOG_DIR) && printf "$(BGreen)Removed $(LOG_DIR)$(Reset)\n"

	# clear exit code with printf
	printf ""
endef


# Make sure help goes first, so if make is called with out any args
# help will be ran
help:
	-@$(help_show)

# print variables for debug information
debug-print:
	-@$(debug_print)

# Run all tests with Pedantic flag on
all-tests:
	-@$(all_tests)

# run tests that are explicitly marked with pytest decorators
marked-tests:
	-@$(marked_tests)

# save all tests to log file
log-tests:
	-@$(log_tests)

# run test functions or methods by function name
filter-tests:
	-@$(filter_tests)

# run manual test code via $USER-runner.py
run:
	-@$(run_runner)

# clean up
clean:
	-@$(clean_gen)


# Target arguments that can be given to the makefile to run a recipe or a 'canned recipe'
.PHONY: help debug-print all-tests marked-tests log-tests filter-tests run clean

# force GNU Make to NOT start a new shell as a subprocess
.ONESHELL:
