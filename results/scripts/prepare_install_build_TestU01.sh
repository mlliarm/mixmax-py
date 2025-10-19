#!/bin/bash
#
# After installation you'll have:
#
#~/TestU01/
#├── bin/           (empty for TestU01)
#├── include/
#│   ├── unif01.h
#│   ├── bbattery.h
#│   ├── swrite.h
#│   └── ... (other headers)
#├── lib/
#│   ├── libtestu01.a
#│   ├── libprobdist.a
#│   ├── libmylib.a
#│   └── ... (other libraries)
#└── share/
#    └── ... (documentation)

set -e # Exit on first error.

# Build prerequisites
echo "Building prerequisites"
sudo apt update
sudo apt install build-essential \
	gcc \
	make \
	autoconf \
	automake \
	libc6-dev \
	#libm-dev

# Build and install TestU01 locally
#
# Installation directory
INSTALL_DIR="$HOME/TestU01"

echo "Installing TestU01 to $INSTALL_DIR..."

# Create directory
mkdir -p "$INSTALL_DIR"

# Download
echo "Downloading..."
cd ~
if [ ! -f "TestU01.zip" ]; then
    echo "Downloading TestU01..."
    wget http://simul.iro.umontreal.ca/testu01/TestU01.zip
fi
echo "Downloaded"

# Extract
echo "Extracting"
if [ ! -d "TestU01-1.2.3" ]; then
    echo "Extracting TestU01..."
    unzip TestU01.zip
fi
echo "Extracted"

# Build and install
cd TestU01-1.2.3
echo "Configuring TestU01..."
./configure --prefix="$INSTALL_DIR"

echo "Building TestU01 (this may take several minutes)..."
make

echo "Installing TestU01..."
make install
echo "Installed."

# Update .bashrc if not already done
echo "Update bash for the first time"
if ! grep -q "# TestU01 paths" ~/.bashrc; then
    echo "" >> ~/.bashrc
    echo "# TestU01 paths" >> ~/.bashrc
    echo "export PATH=\"\$HOME/TestU01/bin:\$PATH\"" >> ~/.bashrc
    echo "export LD_LIBRARY_PATH=\"\$HOME/TestU01/lib:\$LD_LIBRARY_PATH\"" >> ~/.bashrc
    echo "export CPATH=\"\$HOME/TestU01/include:\$CPATH\"" >> ~/.bashrc
    echo "export LIBRARY_PATH=\"\$HOME/TestU01/lib:\$LIBRARY_PATH\"" >> ~/.bashrc
    echo "" >> ~/.bashrc
fi

echo ""
echo "TestU01 installation complete!"
echo "Installation location: $INSTALL_DIR"
echo ""
echo "IMPORTANT: Run the following command to update your environment:"
echo "  source ~/.bashrc"
echo ""
echo "Or close and reopen your terminal."
