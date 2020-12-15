# ______________________
# Author: Matt Williams |
# ----------------------

# Installation Makefile, and development

include config.mk


# standard help procedure
define help_show
	$(_test_env)

	cat << EOF

    [                           The $(PKG_NAME) Installer                               ]

	Command         |                 Description                  |      Usage
	================|==============================================|====================
	help            |    Show this message                         |    make help
	debug-print     |    Print out all variable values             |    make debug-print
	build           |    Build single packaged binary              |    make build
    install         |    Install binary on system                  |    make install
    development     |    Install $(PKG_NAME) for local dev           |    make development

	EOF
endef



define install_development
	$(_test_env)
	printf "\n$(BBlue)Installing $(PKG_NAME) from $(BRANCH) branch$(Reset)\n\n"
	$(PIP) install -r $(DEPENDS)
	if [ "$$?" = 0 ]; then
		printf "\n$(BGreen)$(DEPENDS) installed successfully\nInstalling $(PKG_NAME) locally$(Reset)\n\n"
		$(PIP) install -e .
		if [ "$$?" = 1 ]; then
			printf "\n$(BRed)Failed installing $(PKG_NAME) locally, you must install manually$(Reset)\n" && exit 1
		fi
		exit 0
	else
		printf "\n$(BRed)$(DEPENDS) failed to install, you must install manually$(Reset)\n" && exit 1
	fi
endef

define build_bundle
	printf "Build not implemented yet\n"
endef

define install_locally
	printf "Install not implemented yet\n"
endef



# Make sure help goes first, so if make is called with out any args
# help will be ran
help:
	-@$(help_show)

# print variables for debug information
debug-print:
	-@$(debug_print)

build:
	-@$(build_bundle)

install:
	-@$(install_locally)

development:
	-@$(install_development)


# Target arguments that can be given to the makefile to run a recipe or a 'canned recipe'
.PHONY: help debug-print build install development

# force GNU Make to NOT start a new shell as a subprocess
.ONESHELL:
