from DataChannel import DataChannel


class TestDataChannel:

    def test_constructor(self):
        channel = DataChannel()
        assert channel.title() == ""
        assert channel.unit() == ""
        assert channel.unitValue() == 0
        assert len(channel.data()) == 0


    def test_appendDataTest(self):
        channel = DataChannel()
        channel.append(1.0)
        channel.append(1.5)
        assert len(channel.data()) == 2
        assert channel.data()[0] == 1.0
        assert channel.data()[1] == 1.5
            

    def test_unitTest(self):
        channel = DataChannel()

        channel.setUnit("TestUnit")
        assert channel.unit() == "TestUnit"

    

    def test_unitValueTest(self):
        channel = DataChannel()

        channel.setUnitValue(0)
        assert channel.unitValue() == 0


    def test_titleTest(self):
        channel = DataChannel()

        channel.setTitle("TestTitle")
        assert channel.title() == "TestTitle"

    def test_resetTest(self):
        channel = DataChannel()
        assert channel.title() == ""
        assert channel.unit() == ""
        assert channel.unitValue() == 0
        assert len(channel.data()) == 0




    