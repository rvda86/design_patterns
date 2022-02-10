from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, receiver=None):
        self.receiver = receiver
    
    @abstractmethod
    def execute():
        pass

class OnCommand(Command):
    def execute(self):
        self.receiver.on()

class OffCommand(Command):
    def execute(self):
        self.receiver.off()

class UpCommand(Command):
    def execute(self):
        self.receiver.up()

class DownCommand(Command):
    def execute(self):
        self.receiver.down()

class NextCommand(Command):
    def execute(self):
        self.receiver.next()

class PreviousCommand(Command):
    def execute(self):
        self.receiver.previous()

class NotImplementedCommand(Command):
    def execute(self):
        print("this function is not implemented")

class Television():

    max_volume = 20
    channels = ["TEST", "NPO1", "NPO2", "NPO3", "RTL4", "RTL5"]

    def __init__(self):
        self.tv_on = False
        self.volume = 10
        self.channel = 1

    def on(self):
        if self.tv_on:
            print("the TV is already on")
        else:
            self.tv_on = True
            print("the TV is now on")

    def off(self):
        if not self.tv_on:
            pass
        else:
            self.tv_on = False
            print("the TV is now off")

    def up(self):
        if not self.tv_on:
            pass
        else:
            if self.volume < self.max_volume:
                self.volume += 1
            print(f"the TV volume is now {self.volume}")
            
    def down(self):
        if not self.tv_on:
            pass
        else:
            if self.volume > 0:
                self.volume -= 1
            print(f"the TV volume is now {self.volume}")

    def next(self):
        if not self.tv_on:
            pass
        else: 
            if self.channel == len(self.channels)-1:
                self.channel = 0
            else:
                self.channel += 1
            print(f"the channel has been changed to {self.channels[self.channel]}")

    def previous(self):
        if not self.tv_on:
            pass
        else: 
            if self.channel == 0:
                self.channel = len(self.channels)-1
            else:
                self.channel -= 1
            print(f"the channel has been changed to {self.channels[self.channel]}")

class Radio():

    max_volume = 20
    channels = ["Radio 1", "Radio 2", "3FM", "QMusic", "538", "BNR", "100%NL"]

    def __init__(self):
        self.radio_on = False
        self.volume = 10
        self.channel = 1

    def on(self):
        if self.radio_on:
            print("the radio is already on")
        else:
            self.radio_on = True
            print("the radio is now on")

    def off(self):
        if not self.radio_on:
            pass
        else:
            self.radio_on = False
            print("the radio is now off")

    def up(self):
        if not self.radio_on:
            pass
        else:
            if self.volume < self.max_volume:
                self.volume += 1
            print(f"the radio volume is now {self.volume}")
            
    def down(self):
        if not self.radio_on:
            pass
        else:
            if self.volume > 0:
                self.volume -= 1
            print(f"the radio volume is now {self.volume}")

    def next(self):
        if not self.radio_on:
            pass
        else: 
            if self.channel == len(self.channels)-1:
                self.channel = 0
            else:
                self.channel += 1
            print(f"the channel has been changed to {self.channels[self.channel]}")

    def previous(self):
        if not self.radio_on:
            pass
        else: 
            if self.channel == 0:
                self.channel = len(self.channels)-1
            else:
                self.channel -= 1
            print(f"the channel has been changed to {self.channels[self.channel]}")

class SmartLight():

    max_brightness = 10

    def __init__(self):
        self.light_on = False
        self.brightness = 5

    def on(self):
        if self.light_on:
            print("the light is already on")
        else:
            self.light_on = True
            print("the light is now on")

    def off(self):
        if not self.light_on:
            pass
        else:
            self.light_on = False
            print("the light is now off")

    def up(self):
        if not self.light_on:
            pass
        else:
            if self.brightness < self.max_brightness:
                self.brightness += 1
            print(f"the light brightness is now {self.brightness}")
            
    def down(self):
        if not self.light_on:
            pass
        else:
            if self.brightness > 0:
                self.brightness -= 1
            print(f"the light brightness is now {self.brightness}")

class UniversalRemote():

    def __init__(self, on: Command, off: Command, up: Command, down: Command, next: Command, previous: Command):
        self.on_command = on
        self.off_command = off
        self.up_command = up
        self.down_command = down
        self.next_command = next
        self.previous_command = previous

    def on(self):
        self.on_command.execute()
    def off(self):
        self.off_command.execute()
    def up(self):
        self.up_command.execute()
    def down(self):
        self.down_command.execute()
    def next(self):
        self.next_command.execute()
    def previous(self):
        self.previous_command.execute()

televison = Television()
tv_remote = UniversalRemote(OnCommand(televison),
                            OffCommand(televison),
                            UpCommand(televison),
                            DownCommand(televison),
                            NextCommand(televison),
                            PreviousCommand(televison))
tv_remote.on()
tv_remote.up()
for _ in range(10):
    tv_remote.up()
for _ in range(25):
    tv_remote.down()
for _ in range(10):
    tv_remote.next()
for _ in range(12):
    tv_remote.previous()
tv_remote.off()    
tv_remote.next()

radio = Radio()
radio_remote = UniversalRemote(OnCommand(radio),
                            OffCommand(radio),
                            UpCommand(radio),
                            DownCommand(radio),
                            NextCommand(radio),
                            PreviousCommand(radio))
radio_remote.on()
for _ in range(10):
    radio_remote.up()
for _ in range(25):
    radio_remote.down()
for _ in range(10):
    radio_remote.next()
for _ in range(12):
    radio_remote.previous()
radio_remote.off()    
radio_remote.next()

smart_light = SmartLight()
smart_light_remote =  UniversalRemote(OnCommand(smart_light),
                            OffCommand(smart_light),
                            UpCommand(smart_light),
                            DownCommand(smart_light),
                            NotImplementedCommand(),
                            NotImplementedCommand())

smart_light_remote.on()
for _ in range(10):
    smart_light_remote.up()
for _ in range(11):
    smart_light_remote.down()
smart_light_remote.next()
smart_light_remote.previous()
smart_light_remote.off()    
