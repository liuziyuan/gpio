# gpio
raspberry pi gpio demo

## 传感器符号
- GND: (接地)
- S: 信号位
- VCC: 5V 电源

## GPIO用法解释

### 模式设置
`GPIO.setmode(GPIO.BOARD)`
设置BOARD模式， BOARD是针脚序号，用树莓派GPIO对照表对照即可

`GPIO.setmode(GPIO.BCM)`
设置为BCM模式，BCM用的是P码，用树莓派GPIO对照表对照即可

### 针脚设置
`GPIO.setup(38, GPIO.OUT)`
针脚设置，38代表的是针脚的号码，GPIO.IN 是输入，GPIO.OUT是输出。

所有的传感器的数据都属于输入或输出

### 输出设置
`GPIO.output(38, GPIO.HIGH)`
描述针脚38输出HGIH值，GPIO.HIGH or GPIO.LOW

### 温湿度传感器
参考 https://github.com/szazo/DHT11_Python

