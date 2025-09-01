#!/usr/bin/env python3
"""
AIOS Comprehensive Menu System
A user-friendly interface for AIOS (AGI Research) with full functionality
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path


class AIOSMenu:
    def __init__(self):
        self.base_dir = Path("/home/booze/ai-development")
        self.env_path = self.base_dir / "environments" / "aios-env"
        self.activate_script = self.env_path / "bin" / "activate"
        self.config_dir = Path.home() / ".aios"

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system("clear" if os.name == "posix" else "cls")

    def print_banner(self):
        """Print the AIOS banner"""
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                           🚀 AIOS (AGI Research) 🚀                          ║
║                    Advanced AI Agent Operating System                        ║
║                        Comprehensive Development Menu                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)

    def print_menu(self):
        """Print the main menu options"""
        menu = """
📋 MAIN MENU - Choose an option:

🔧 CORE AIOS OPERATIONS:
  1. 🐍 Interactive AIOS Python Shell
  2. 🧪 Test AIOS Installation & Components
  3. 📚 View AIOS Documentation & Examples
  4. ⚙️  AIOS Configuration & Settings

🤖 AI AGENT DEVELOPMENT:
  5. 🏗️  Create New AI Agent
  6. 🔄 Run AIOS Builder Agent
  7. 📊 Agent Status & Monitoring
  8. 🎯 Agent Workflow Management

🛠️ DEVELOPMENT TOOLS:
  9. 📁 Open Project Directory
  10. 🔍 Debug AIOS System
  11. 📦 Package Management
  12. 🧹 System Cleanup & Maintenance

🌐 AI STACK INTEGRATION:
  13. 🚀 Setup Complete AI Development Stack
  14. 🔗 AI Stack Status & Integration
  15. 📈 Performance Monitoring

💻 SYSTEM OPERATIONS:
  16. 🔄 Restart AIOS Environment
  17. 📋 System Information
  18. 🆘 Troubleshooting & Help
  19. 🚪 Exit

Enter your choice (1-19): """
        return input(menu)

    def activate_environment(self):
        """Activate the AIOS virtual environment"""
        if not self.activate_script.exists():
            print("❌ AIOS environment not found!")
            return False

        # Set environment variables
        os.environ["VIRTUAL_ENV"] = str(self.env_path)
        os.environ["PATH"] = f"{self.env_path}/bin:{os.environ.get('PATH', '')}"
        return True

    def run_python_shell(self):
        """Run interactive AIOS Python shell"""
        print("\n🐍 Starting AIOS Interactive Python Shell...")
        print("📝 Available imports: import aios")
        print("📝 Example: obj = aios.Object('MyAgent')")
        print("📝 Type 'exit()' to return to menu\n")

        if self.activate_environment():
            try:
                subprocess.run([f"{self.env_path}/bin/python"], check=True)
            except subprocess.CalledProcessError:
                print("❌ Failed to start Python shell")
        else:
            print("❌ Environment activation failed")

    def test_aios_installation(self):
        """Test AIOS installation and components"""
        print("\n🧪 Testing AIOS Installation...")

        if not self.activate_environment():
            print("❌ Environment activation failed")
            return

        test_script = """
import aios
print("✅ AIOS imported successfully")

# Test Object class
obj = aios.Object("TestAgent")
print(f"✅ Object created: {obj}")

# Test State class
state = aios.State(["idle", "working", "done"])
print(f"✅ State created: {state}")
state.change("working")
print(f"✅ State changed to: {state.current_state}")

print("🎉 All AIOS components working correctly!")
"""

        try:
            result = subprocess.run(
                [f"{self.env_path}/bin/python", "-c", test_script],
                capture_output=True,
                text=True,
                check=True,
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"❌ Test failed: {e}")
            print(f"Error output: {e.stderr}")

    def show_documentation(self):
        """Show AIOS documentation and examples"""
        print("\n📚 AIOS Documentation & Examples")
        print("=" * 50)

        docs = """
📖 AIOS CORE CONCEPTS:

🔹 Object Class:
   - Represents AI agents and entities
   - Properties: name, id, created_at, properties
   - Methods: update(), get_property(), set_property()

🔹 State Class:
   - Manages agent state transitions
   - Properties: states, current_state, history
   - Methods: change(), can_change(), get_history()

📝 BASIC USAGE EXAMPLES:

1. Create an agent:
   obj = aios.Object("MyAgent")
   obj.set_property("role", "researcher")

2. Manage state:
   state = aios.State(["idle", "working", "done"])
   state.change("working")

3. Agent workflow:
   agent = aios.Object("TaskAgent")
   workflow = aios.State(["start", "process", "complete"])
   workflow.change("process")

🔗 RESOURCES:
   - GitHub: https://github.com/agiresearch/AIOS
   - Documentation: Check project README
   - Examples: See test_agent.py in project directory
"""
        print(docs)
        input("\nPress Enter to continue...")

    def create_agent(self):
        """Create a new AI agent"""
        print("\n🏗️ Create New AI Agent")
        print("=" * 30)

        name = input("Enter agent name: ").strip()
        if not name:
            print("❌ Agent name is required")
            return

        agent_type = input(
            "Enter agent type (researcher/coder/analyst/assistant): "
        ).strip()
        properties = {}

        print("\n📝 Configure agent properties (press Enter to skip):")
        while True:
            key = input("Property name (or Enter to finish): ").strip()
            if not key:
                break
            value = input(f"Value for {key}: ").strip()
            properties[key] = value

        # Create agent file
        agent_file = self.base_dir / f"{name.lower()}_agent.py"
        agent_code = f'''#!/usr/bin/env python3
"""
{name} Agent
AIOS Agent Implementation
"""

import aios
import time

class {name}Agent:
    def __init__(self):
        self.obj = aios.Object("{name}")
        self.state = aios.State(["idle", "working", "complete", "error"])

        # Set properties
        self.obj.set_property("type", "{agent_type}")
        for key, value in {properties}:
            self.obj.set_property(key, value)

    def start(self):
        """Start the agent workflow"""
        print(f"🚀 Starting {{self.obj.name}}...")
        self.state.change("working")

        try:
            # Agent logic here
            print(f"✅ {{self.obj.name}} is working...")
            time.sleep(1)

            self.state.change("complete")
            print(f"✅ {{self.obj.name}} completed successfully!")

        except Exception as e:
            self.state.change("error")
            print(f"❌ {{self.obj.name}} encountered an error: {{e}}")

    def get_status(self):
        """Get current agent status"""
        return {{
            "name": self.obj.name,
            "state": self.state.current_state,
            "properties": self.obj.properties
        }}

if __name__ == "__main__":
    agent = {name}Agent()
    agent.start()
    print("\\n📊 Agent Status:", agent.get_status())
'''

        try:
            with open(agent_file, "w") as f:
                f.write(agent_code)

            # Make executable
            os.chmod(agent_file, 0o755)

            print(f"✅ Agent created: {agent_file}")
            print(f"🚀 Run with: python {agent_file}")

        except Exception as e:
            print(f"❌ Failed to create agent: {e}")

    def run_builder_agent(self):
        """Run the AIOS Builder Agent"""
        print("\n🔄 Running AIOS Builder Agent...")

        builder_script = self.base_dir / "aios_builder_agent.py"
        if not builder_script.exists():
            print("❌ AIOS Builder Agent not found!")
            return

        if self.activate_environment():
            try:
                subprocess.run(
                    [f"{self.env_path}/bin/python", str(builder_script)], check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"❌ Builder agent failed: {e}")
        else:
            print("❌ Environment activation failed")

    def show_agent_status(self):
        """Show agent status and monitoring"""
        print("\n📊 Agent Status & Monitoring")
        print("=" * 35)

        # Find agent files
        agent_files = list(self.base_dir.glob("*_agent.py"))

        if not agent_files:
            print("📭 No agents found")
            return

        print(f"🔍 Found {len(agent_files)} agents:")
        for agent_file in agent_files:
            print(f"  • {agent_file.name}")

        # Show system status
        print(f"\n📈 System Status:")
        print(
            f"  • AIOS Environment: {'✅ Active' if self.env_path.exists() else '❌ Not found'}"
        )
        print(f"  • Python Version: {sys.version.split()[0]}")
        print(f"  • Working Directory: {self.base_dir}")

    def open_project_directory(self):
        """Open project directory in file manager"""
        print(f"\n📁 Opening project directory: {self.base_dir}")

        try:
            if os.name == "posix":
                subprocess.run(["xdg-open", str(self.base_dir)], check=True)
            else:
                subprocess.run(["explorer", str(self.base_dir)], check=True)
            print("✅ Project directory opened")
        except subprocess.CalledProcessError:
            print("❌ Failed to open directory")

    def debug_system(self):
        """Debug AIOS system"""
        print("\n🔍 Debugging AIOS System...")

        debug_script = self.base_dir / "debug_aios.py"
        if not debug_script.exists():
            print("❌ Debug script not found!")
            return

        if self.activate_environment():
            try:
                subprocess.run(
                    [f"{self.env_path}/bin/python", str(debug_script)], check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"❌ Debug failed: {e}")
        else:
            print("❌ Environment activation failed")

    def package_management(self):
        """Package management menu"""
        print("\n📦 Package Management")
        print("=" * 25)

        while True:
            choice = input(
                """
1. 📋 List installed packages
2. 🔍 Search packages
3. 📥 Install package
4. 🗑️ Uninstall package
5. 🔄 Update packages
6. ↩️ Back to main menu

Enter choice (1-6): """
            )

            if choice == "1":
                self.list_packages()
            elif choice == "2":
                self.search_packages()
            elif choice == "3":
                self.install_package()
            elif choice == "4":
                self.uninstall_package()
            elif choice == "5":
                self.update_packages()
            elif choice == "6":
                break
            else:
                print("❌ Invalid choice")

    def list_packages(self):
        """List installed packages"""
        if self.activate_environment():
            try:
                result = subprocess.run(
                    [f"{self.env_path}/bin/pip", "list"],
                    capture_output=True,
                    text=True,
                    check=True,
                )
                print("\n📋 Installed Packages:")
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to list packages: {e}")

    def search_packages(self):
        """Search for packages"""
        query = input("Enter package name to search: ").strip()
        if not query:
            return

        if self.activate_environment():
            try:
                result = subprocess.run(
                    [f"{self.env_path}/bin/pip", "search", query],
                    capture_output=True,
                    text=True,
                    check=True,
                )
                print(f"\n🔍 Search results for '{query}':")
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"❌ Search failed: {e}")

    def install_package(self):
        """Install a package"""
        package = input("Enter package name to install: ").strip()
        if not package:
            return

        if self.activate_environment():
            try:
                subprocess.run(
                    [f"{self.env_path}/bin/pip", "install", package], check=True
                )
                print(f"✅ Package '{package}' installed successfully")
            except subprocess.CalledProcessError as e:
                print(f"❌ Installation failed: {e}")

    def uninstall_package(self):
        """Uninstall a package"""
        package = input("Enter package name to uninstall: ").strip()
        if not package:
            return

        if self.activate_environment():
            try:
                subprocess.run(
                    [f"{self.env_path}/bin/pip", "uninstall", "-y", package], check=True
                )
                print(f"✅ Package '{package}' uninstalled successfully")
            except subprocess.CalledProcessError as e:
                print(f"❌ Uninstallation failed: {e}")

    def update_packages(self):
        """Update packages"""
        if self.activate_environment():
            try:
                subprocess.run(
                    [f"{self.env_path}/bin/pip", "install", "--upgrade", "pip"],
                    check=True,
                )
                print("✅ pip updated successfully")
            except subprocess.CalledProcessError as e:
                print(f"❌ Update failed: {e}")

    def setup_ai_stack(self):
        """Setup complete AI development stack"""
        print("\n🚀 Setting up Complete AI Development Stack...")

        stack_script = self.base_dir / "ai_stack_master.py"
        if not stack_script.exists():
            print("❌ AI Stack setup script not found!")
            return

        if self.activate_environment():
            try:
                subprocess.run(
                    [f"{self.env_path}/bin/python", str(stack_script)], check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"❌ AI Stack setup failed: {e}")
        else:
            print("❌ Environment activation failed")

    def show_ai_stack_status(self):
        """Show AI stack status and integration"""
        print("\n🔗 AI Stack Status & Integration")
        print("=" * 35)

        ai_stack_dir = self.base_dir / "ai-stack"
        if ai_stack_dir.exists():
            print("✅ AI Stack directory found")

            # Check for key components
            components = [
                ("LangChain", "langchain"),
                ("AutoGen", "autogen"),
                ("Transformers", "transformers"),
                ("PyTorch", "torch"),
                ("TensorFlow", "tensorflow"),
                ("Ollama", "ollama"),
            ]

            print("\n📊 Component Status:")
            for name, module in components:
                try:
                    __import__(module)
                    print(f"  ✅ {name}")
                except ImportError:
                    print(f"  ❌ {name}")
        else:
            print("❌ AI Stack not installed")
            print("💡 Run option 13 to install AI Stack")

    def restart_environment(self):
        """Restart AIOS environment"""
        print("\n🔄 Restarting AIOS Environment...")

        if self.activate_environment():
            print("✅ Environment restarted successfully")
        else:
            print("❌ Failed to restart environment")

    def show_system_info(self):
        """Show system information"""
        print("\n📋 System Information")
        print("=" * 25)

        import platform

        print(f"🖥️  OS: {platform.system()} {platform.release()}")
        print(f"🐍 Python: {sys.version}")
        print(f"📁 AIOS Directory: {self.base_dir}")
        print(f"🔧 Environment: {self.env_path}")
        print(f"👤 User: {os.getenv('USER', 'Unknown')}")
        print(f"🏠 Home: {Path.home()}")

        # Check GPU
        try:
            result = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
            if result.returncode == 0:
                print("🎮 GPU: NVIDIA GPU detected")
            else:
                print("🎮 GPU: No NVIDIA GPU detected")
        except FileNotFoundError:
            print("🎮 GPU: nvidia-smi not available")

    def troubleshooting(self):
        """Troubleshooting and help"""
        print("\n🆘 Troubleshooting & Help")
        print("=" * 30)

        help_text = """
🔧 COMMON ISSUES & SOLUTIONS:

❌ "AIOS environment not found"
   Solution: Run the installation script again

❌ "ImportError: No module named 'aios'"
   Solution: Activate environment: source environments/aios-env/bin/activate

❌ "Permission denied"
   Solution: Check file permissions and ownership

❌ "Network connection failed"
   Solution: Check internet connection and try again

📞 SUPPORT:
   - GitHub Issues: https://github.com/agiresearch/AIOS/issues
   - Documentation: Check project README
   - Community: Join AIOS Discord/Telegram

🛠️ USEFUL COMMANDS:
   - Test AIOS: python debug_aios.py
   - Activate env: source environments/aios-env/bin/activate
   - List packages: pip list
   - Update pip: pip install --upgrade pip
"""
        print(help_text)
        input("\nPress Enter to continue...")

    def run(self):
        """Main menu loop"""
        while True:
            self.clear_screen()
            self.print_banner()

            choice = self.print_menu()

            if choice == "1":
                self.run_python_shell()
            elif choice == "2":
                self.test_aios_installation()
            elif choice == "3":
                self.show_documentation()
            elif choice == "4":
                print("⚙️ Configuration menu - Coming soon!")
                input("Press Enter to continue...")
            elif choice == "5":
                self.create_agent()
            elif choice == "6":
                self.run_builder_agent()
            elif choice == "7":
                self.show_agent_status()
            elif choice == "8":
                print("🎯 Workflow management - Coming soon!")
                input("Press Enter to continue...")
            elif choice == "9":
                self.open_project_directory()
            elif choice == "10":
                self.debug_system()
            elif choice == "11":
                self.package_management()
            elif choice == "12":
                print("🧹 Cleanup - Coming soon!")
                input("Press Enter to continue...")
            elif choice == "13":
                self.setup_ai_stack()
            elif choice == "14":
                self.show_ai_stack_status()
            elif choice == "15":
                print("📈 Performance monitoring - Coming soon!")
                input("Press Enter to continue...")
            elif choice == "16":
                self.restart_environment()
            elif choice == "17":
                self.show_system_info()
            elif choice == "18":
                self.troubleshooting()
            elif choice == "19":
                print("\n👋 Thank you for using AIOS!")
                print("🚀 Happy AI development!")
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)


if __name__ == "__main__":
    menu = AIOSMenu()
    menu.run()
