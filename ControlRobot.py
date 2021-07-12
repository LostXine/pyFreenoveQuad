from Communication import *


class ControlRobot:

    def __init__(self, comm):
        self.comm = comm
    
    def set_boot_state(self):
        self.comm.send_command([Orders.requestBootState])
        
    def set_calibrate_state(self):
        self.comm.send_command([Orders.requestCalibrateState])
        
    def set_install_state(self):
        self.comm.send_command([Orders.requestInstallState])
        
    def set_active_mode(self):
        self.comm.send_command([Orders.requestActiveMode])
        
    def set_switch_mode(self):
        self.comm.send_command([Orders.requestSwitchMode])
        
    def set_sleep_mode(self):
        self.comm.send_command([Orders.requestSleepMode])

    def get_voltage(self):
        inData = self.comm.send_command([Orders.requestSupplyVoltage])
        
        if len(inData) > 2:
            if inData[0] == Orders.supplyVoltage:
                return (inData[1] * 128 + inData[2]) / 100.0
        return 0
        
    def move_leg(self, leg, dx, dy, dz):
        self.comm.send_command([Orders.requestMoveLeg, leg, 64 + dx, 64 + dy, 64 + dz])
    
    
    
if __name__ == '__main__':
    # ser = serial.Serial(port='COM6', baudrate=115200, timeout=0.5)
    ser = TcpConnection()
    time.sleep(5)
    
    con = Communication(ser)
    con.open()
    
    roc = ControlRobot(con)
    roc.set_boot_state()
    time.sleep(1)
    for i in range(4):
        roc.move_leg(i + 1, 0, 0, 10)
        time.sleep(1)
        print(roc.get_voltage())
    # roc.set_boot_state()
    con.close()
        
        
        
