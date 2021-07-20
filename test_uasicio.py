import uasyncio

async def text1(text,time):
    while True:
        print(text)
        import utime
        import machine
        Filtrace = machine.Pin(15, machine.Pin.OUT)
        Filtrace.on()
        utime.sleep(1)
        Filtrace.off()
        await uasyncio.sleep_ms(time)

async def text2(text,time):
    while True:
        print(text)
        await uasyncio.sleep_ms(time)

async def main():
    while True:
        print("Plannig started")

        print("Tasks canceled")
        uasyncio.create_task(text1("Jan Vasko",10000))
        uasyncio.create_task(text2("Andrea Vasko",5000))
        await uasyncio.sleep_ms(100000)
        uasyncio.Task.cancel()
        text2.cancel()
        print("Plannig Finished")

# Running on a generic board
uasyncio.run(main())



import uasyncio
uasyncio.Task.cancel()