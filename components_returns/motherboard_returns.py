import subprocess

class MotherboardReturns():
    def __init__(self):
        pass

    def get_motherboard_info(self):
        try:
            result = subprocess.run(['sudo', 'dmidecode', '-t', '2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            if result.returncode == 0:
                return result.stdout
            else:
                return "error"
        except Exception as e:
            return f"Erro: {str(e)}"