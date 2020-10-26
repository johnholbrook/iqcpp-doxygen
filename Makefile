vexcode_iq_version := $(shell defaults read /Applications/VEXcode\ IQ.app/Contents/Info.plist CFBundleVersion)

all: clean
	echo "PROJECT_NUMBER = \"Unofficial documentation for version $(vexcode_iq_version)\"" >> doxygen_config
	doxygen doxygen_config
	python3 add_index_content.py

clean:
	rm -rf docs