#!/usr/bin/env python3
"""Setup script for GitHub Copilot CLI Examples."""

import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.11 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print("❌ Python 3.11 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True


def verify_structure():
    """Verify repository structure."""
    required_dirs = [
        'challenges/easy',
        'challenges/medium',
        'challenges/hard',
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
    
    # Success message
    print("\n" + "=" * 50)
    print("✨ Setup complete!")
    print("\n📖 Next steps:")
    print("   1. Read docs/GETTING_STARTED.md")
    print("   2. Explore the challenges in the challenges/ directory")
    print("   3. Run: python validate.py")


if __name__ == "__main__":
    main()
