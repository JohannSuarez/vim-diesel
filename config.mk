# ______________________
# Author: Matt Williams |
# ----------------------

# Configuration file for all make files
# Shared Global variables will go here


# ANSI Escape code colors
BBlack 	:= $(shell echo "\033[1;30m")
BRed 	:= $(shell echo "\033[1;31m")
BGreen 	:= $(shell echo "\033[1;32m")
BYellow := $(shell echo "\033[1;33m")
BBlue 	:= $(shell echo "\033[1;34m")
BPurple := $(shell echo "\033[1;35m")
BCyan 	:= $(shell echo "\033[1;36m")
BWhite 	:= $(shell echo "\033[1;37m")
Reset 	:= $(shell echo "\033[0m")


# GNU Make globals, use 'Simply expanded variable assignment syntax'
# ===================================
SHELL           ?= /bin/sh
ENV             := $$VIRTUAL_ENV
ENV_BIN         += $(ENV)/bin
PY_TEST         += $(ENV_BIN)/pytest
PY_INSTALLER    += $(ENV_BIN)/pyinstaller
PIP             += $(ENV_BIN)/pip
PY_INTERP       += $(ENV_BIN)/python3
CURR_DIR        := $(shell basename `pwd`)
REPO_NAME       := $(shell basename `git rev-parse --show-toplevel`)

ifeq ($(CURR_DIR), $(REPO_NAME))
	PKG_NAME    := $(shell $(PY_INTERP) setup.py --name)
	VERSION     := $(shell $(PY_INTERP) setup.py --version)
else
	PKG_NAME    := $(shell cd .. && $(PY_INTERP) setup.py --name)
	VERSION     := $(shell cd .. && $(PY_INTERP) setup.py --version)
endif

DEPENDS   		:= requirements/dependencies.txt
BRANCH          := $(shell basename `git symbolic-ref HEAD`)

# Pytest argument variables
VERBOSE         := -v
REASON          := -r
SKIPPED         := -s
FILTER          := -k	# requires argument
MARKED          := -m	# requires argument
SHOW_FIXTURES   := --setup-show
TRACE_BACK      := --tb=short
PEDANTIC        := $(VERBOSE) $(SHOW_FIXTURES) $(TRACE_BACK)

# Global Procedures

# Test to see if users Virtual Env is activated, also check for foxhound specific environment variables
define _test_env =
	[ -z $(ENV) ] && printf "$(BRed)You have not activated your virtual environment ... exiting\n$(Reset)" && exit 0
endef


# Print out all populated runtime variables
define debug_print
	$(_test_env)
	printf "$(BWhite)Shell: $(Reset)$(BGreen)$(SHELL)$(Reset)\n"
	printf "$(BWhite)User: $(Reset)$(BGreen)$(USER)$(Reset)\n"
	printf "$(BWhite)Virtual environment: $(Reset)$(BGreen)$(ENV)$(Reset)\n"
	printf "$(BWhite)Bin: $(Reset)$(BGreen)$(ENV_BIN)$(Reset)\n"
	printf "$(BWhite)Pip: $(Reset)$(BGreen)$(PIP)$(Reset)\n"
	printf "$(BWhite)Python: $(Reset)$(BGreen)$(PY_INTERP)$(Reset)\n"
	printf "$(BWhite)Pytest: $(Reset)$(BGreen)$(PY_TEST)$(Reset)\n"
	printf "$(BWhite)Pyinstaller: $(Reset)$(BGreen)$(PY_INSTALLER)$(Reset)\n"
	printf "$(BWhite)Package Name: $(Reset)$(BGreen)$(PKG_NAME)$(Reset)\n"
	printf "$(BWhite)Version: $(Reset)$(BGreen)$(VERSION)$(Reset)\n"
	printf "$(BWhite)Depencies file: $(Reset)$(BGreen)$(DEPENDS)$(Reset)\n"
	printf "$(BWhite)Current Branch: $(Reset)$(BGreen)$(BRANCH)$(Reset)\n"
	printf "$(BWhite)Verbose flag: $(Reset)$(BGreen)$(VERBOSE)$(Reset)\n"
	printf "$(BWhite)Reason flag: $(Reset)$(BGreen)$(REASON)$(Reset)\n"
	printf "$(BWhite)Skipped flag: $(Reset)$(BGreen)$(SKIPPED)$(Reset)\n"
	printf "$(BWhite)Filter flag: $(Reset)$(BGreen)$(FILTER)$(Reset)\n"
	printf "$(BWhite)Marked flag: $(Reset)$(BGreen)$(MARKED)$(Reset)\n"
	printf "$(BWhite)Fixture flag: $(Reset)$(BGreen)$(SHOW_FIXTURES)$(Reset)\n"
	printf "$(BWhite)Traceback flag: $(Reset)$(BGreen)$(TRACE_BACK)$(Reset)\n"
	printf "$(BWhite)Pedantic: $(Reset)$(BGreen)$(PEDANTIC)$(Reset)\n"
	printf "$(BWhite)Runner file: $(Reset)$(BGreen)$(RUNNER_FILE)$(Reset)\n"
endef
