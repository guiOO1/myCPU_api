import subprocess

class MotherboardReturns():
    def __init__(self):
        pass

    def get_motherboard_info(self):
        try:
            result = subprocess.run(['sudo', 'dmidecode', '-t', '2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            if result.returncode == 0:
                self.motherboard_manufacturer = result.stdout.splitlines()[6]
                self.motherboard_model_name = result.stdout.splitlines()[7]
            else:
                self.motherboard_manufacturer = "NaN"
                self.motherboard_model_name = "NaN"

        except Exception as e:
            print(f"Erro: {str(e)}")

    def get_motherboard_manufacturer(self):
        self.get_motherboard_info()

        return self.motherboard_manufacturer[15:]

    def get_motherboard_model_name(self):
        self.get_motherboard_info()

        return self.motherboard_model_name[15:]