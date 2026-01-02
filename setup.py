#!/usr/bin/env python3
"""
Setup script for GitHub Copilot CLI Examples
Validates Python environment and installs dependencies
"""

import subprocess
import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True


def install_dependencies():
    """Install required Python packages."""
    packages = ['requests', 'beautifulsoup4']
    
    print("\n📦 Installing Python dependencies...")
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '--quiet', '--upgrade', 'pip'
        ])
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '--quiet', *packages
        ])
        print("✅ All dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def check_nodejs():
    """Check if Node.js is available."""
    try:
        result = subprocess.run(
            ['node', '--version'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✅ Node.js version: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        # Node.js not installed, which is acceptable since it's optional
        pass
    
    print("⚠️  Node.js not found (optional, needed for JavaScript examples)")
    return False


def check_go():
    """Check if Go is available."""
    try:
        result = subprocess.run(
            ['go', 'version'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            version = result.stdout.strip().replace('go version ', '')
            print(f"✅ Go version: {version}")
            return True
    except FileNotFoundError:
        # Go not installed, which is acceptable since it's optional
        pass
    
    print("⚠️  Go not found (optional, needed for Go examples)")
    return False


def verify_structure():
    """Verify repository structure."""
    required_dirs = [
        'skills/python',
        'skills/javascript',
        'skills/go',
        'challenges/easy',
        'challenges/medium',
        'challenges/hard',
        'examples',
        'docs'
    ]
    
    print("\n📁 Verifying repository structure...")
    all_present = True
    for dir_path in required_dirs:
        path = Path(dir_path)
        if path.exists() and path.is_dir():
            print(f"✅ {dir_path}/")
        else:
            print(f"❌ {dir_path}/ (missing)")
            all_present = False
    
    return all_present


def main():
    """Run setup and validation."""
    print("🚀 GitHub Copilot CLI Examples - Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Verify repository structure
    if not verify_structure():
        print("\n⚠️  Some directories are missing")
        print("   Make sure you're in the repository root")
    
    # Install Python dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check optional dependencies
    print("\n🔍 Checking optional dependencies...")
    check_nodejs()
    check_go()
    
    # Success message
    print("\n" + "=" * 50)
    print("✨ Setup complete!")
    print("\n📖 Next steps:")
    print("   1. Read docs/GETTING_STARTED.md")
    print("   2. Try: python skills/python/basic_functions.py")
    print("   3. Run: python validate.py (to test all examples)")
    print("   4. Explore challenges and examples")


if __name__ == "__main__":
    main()
