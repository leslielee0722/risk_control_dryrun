#!/usr/bin/env python3
import subprocess
import sys
import os
import signal
import time
from pathlib import Path
from dotenv import load_dotenv

class ServiceManager:
    def __init__(self):
        self.processes = []
        self.project_root = Path(__file__).parent
        load_dotenv()
        self.server_ip = os.getenv('SERVER_IP', 'localhost')
        self.static_port = os.getenv('STATIC_SERVER_PORT', '9090')
        self.flask_port = os.getenv('FLASK_SERVER_PORT', '8465')
        
    def print_header(self):
        print("=" * 60)
        print("企业信用风险智能评估演示系统 - 服务启动器")
        print("=" * 60)
        print()
    
    def print_service_info(self, name, url, description):
        print(f"服务名称: {name}")
        print(f"访问地址: {url}")
        print(f"功能描述: {description}")
        print("-" * 60)
    
    def check_dependencies(self):
        print("检查依赖...")
        try:
            import flask
            import livereload
            print("✓ 所有依赖已安装")
            print()
            return True
        except ImportError as e:
            print(f"✗ 缺少依赖: {e}")
            print("请运行: pip install -r requirements.txt")
            print()
            return False
    
    def start_static_server(self):
        print(f"正在启动静态页面服务器 (端口 {self.static_port})...")
        try:
            # 使用Python内置的http.server来启动静态页面服务器
            process = subprocess.Popen(
                [sys.executable, "-m", "http.server", self.static_port],
                cwd=self.project_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.processes.append(("静态页面服务器", process))
            print("✓ 静态页面服务器启动成功")
            return True
        except Exception as e:
            print(f"✗ 静态页面服务器启动失败: {e}")
            return False
    
    def start_flask_app(self):
        print("正在启动Flask应用 (端口 5005)...")
        flask_dir = self.project_root / "development_platform"
        try:
            process = subprocess.Popen(
                [sys.executable, "run.py"],
                cwd=flask_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.processes.append(("Flask应用", process))
            print("✓ Flask应用启动成功")
            return True
        except Exception as e:
            print(f"✗ Flask应用启动失败: {e}")
            return False
    
    def wait_for_services(self):
        print()
        print("等待服务启动...")
        time.sleep(3)
        
        all_running = True
        for name, process in self.processes:
            if process.poll() is not None:
                print(f"✗ {name} 已停止")
                all_running = False
            else:
                print(f"✓ {name} 运行中")
        
        return all_running
    
    def print_access_info(self):
        print()
        print("=" * 60)
        print("所有服务已启动！")
        print("=" * 60)
        print()
        
        print("访问地址:")
        print()
        self.print_service_info(
            "总览页面",
            f"http://{self.server_ip}:{self.static_port}",
            "系统入口，展示业务流程和模块导航"
        )
        print()
        self.print_service_info(
            "开发平台",
            f"http://{self.server_ip}:{self.flask_port}",
            "数据工程和模型训练平台"
        )
        print()
        print("其他模块:")
        print(f"  - 告警清单: http://{self.server_ip}:{self.static_port}/headquarters_alarm_list/headquarters_alarm_list.html")
        print(f"  - 预警服务: http://{self.server_ip}:{self.static_port}/warning_service_platform/warning_service_platform_v5.html")
        print(f"  - 运营平台: http://{self.server_ip}:{self.static_port}/operations_platform/operations_paltform.html")
        print()
        print("=" * 60)
        print("按 Ctrl+C 停止所有服务")
        print("=" * 60)
    
    def stop_all_services(self):
        print()
        print("正在停止所有服务...")
        for name, process in self.processes:
            try:
                process.terminate()
                process.wait(timeout=5)
                print(f"✓ {name} 已停止")
            except subprocess.TimeoutExpired:
                process.kill()
                print(f"✓ {name} 已强制停止")
            except Exception as e:
                print(f"✗ 停止 {name} 时出错: {e}")
        print("所有服务已停止")
    
    def run(self):
        self.print_header()
        
        if not self.check_dependencies():
            sys.exit(1)
        
        print("启动服务...")
        print("-" * 60)
        
        # 首先启动Flask服务
        print(f"正在启动Flask应用 (端口 {self.flask_port})...")
        flask_dir = self.project_root / "development_platform"
        try:
            # 设置环境变量，传递给Flask应用
            env = os.environ.copy()
            env['SERVER_IP'] = self.server_ip
            env['STATIC_SERVER_PORT'] = str(self.static_port)
            env['FLASK_SERVER_PORT'] = str(self.flask_port)
            
            flask_process = subprocess.Popen(
                [sys.executable, "run.py"],
                cwd=flask_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=env
            )
            self.processes.append(("Flask应用", flask_process))
            print("✓ Flask应用启动成功")
            
            # 等待Flask服务完全启动
            print("等待Flask服务完全启动...")
            time.sleep(3)
            
            # 检查Flask服务是否正常运行
            if flask_process.poll() is None:
                print("✓ Flask应用运行正常")
            else:
                print("✗ Flask应用启动后立即停止")
                self.stop_all_services()
                sys.exit(1)
            
        except Exception as e:
            print(f"✗ Flask应用启动失败: {e}")
            self.stop_all_services()
            sys.exit(1)
        
        # 然后启动静态页面服务器
        print(f"\n正在启动静态页面服务器 (端口 {self.static_port})...")
        try:
            # 使用Python内置的http.server来启动静态页面服务器
            static_process = subprocess.Popen(
                [sys.executable, "-m", "http.server", self.static_port],
                cwd=self.project_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.processes.append(("静态页面服务器", static_process))
            print("✓ 静态页面服务器启动成功")
            
            # 等待静态页面服务器完全启动
            print("等待静态页面服务器完全启动...")
            time.sleep(2)
            
            # 检查静态页面服务器是否正常运行
            if static_process.poll() is not None:
                print("✗ 静态页面服务器启动后立即停止")
                self.stop_all_services()
                sys.exit(1)
            print("✓ 静态页面服务器运行正常")
            
        except Exception as e:
            print(f"✗ 静态页面服务器启动失败: {e}")
            self.stop_all_services()
            sys.exit(1)
        
        self.print_access_info()
        
        try:
            while True:
                for name, process in self.processes:
                    if process.poll() is not None:
                        print(f"警告: {name} 已意外停止")
                        self.stop_all_services()
                        sys.exit(1)
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_all_services()
            sys.exit(0)

def main():
    manager = ServiceManager()
    manager.run()

if __name__ == "__main__":
    main()
