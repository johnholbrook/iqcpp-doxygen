vexcode_iq_version := $(shell defaults read /Applications/VEXcode\ IQ.app/Contents/Info.plist CFBundleVersion)

all: clean
	echo "PROJECT_NUMBER = $(vexcode_iq_version)" >> doxygen_config
	doxygen doxygen_config

clean:
	rm -rf docs