from DataParser import DataParser

class TestDataParser:

    # constructor test
    def test_constructor(self):
        parser = DataParser()

        assert parser.title() == ""
        assert parser.unit() == "s"
        assert parser.unitValue() == 1

    def test_unitSplitterEmpty(self):
        parser = DataParser()

        inputLine = ""
        parser.unitsplitter(inputLine)
        assert parser.unit() == "s"
        assert parser.unitValue() == 1

    def test_unitSplitterSimple(self):
        parser = DataParser()

        inputLine = "[ms];1000"
        parser.unitsplitter(inputLine)
        assert parser.unit() == "ms"
        assert parser.unitValue() == 1000

    def test_unitSplitterEnd(self):
        parser = DataParser()

        inputLine = "blabla[V];5"
        parser.unitsplitter(inputLine)
        assert parser.unit() == "V"
        assert parser.unitValue() == 5

    def test_unitSplitterMid(self):
        parser = DataParser()

        inputLine = "blabla[V];ewr5bla"
        parser.unitsplitter(inputLine)
        assert parser.unit() == "V"
        assert parser.unitValue() == 5

    def test_unitSplittterQuater(self):
        parser = DataParser()

        inputLine = "sdad[ms]gg;;sd1000s;a"
        parser.unitsplitter(inputLine)
        assert parser.unit() == "ms"
        assert parser.unitValue() == 1000


    def test_parseDataLine_unitLine(self):
        parser = DataParser()

        dataList = []
        inputLine = "[ms];1000"
        parser.parseDataLine(inputLine, dataList)
        assert parser.unit() == "ms"
        assert parser.unitValue() == 1000
        assert len(dataList) == 0

    def test_parseDataLine_SingleDataLine(self):
        parser = DataParser()

        dataList = []
        inputLine = "0;1.0;2.0;3.0;4.0;"
        parser.parseDataLine(inputLine, dataList)
        assert parser.unit() == "s"
        assert parser.unitValue() == 1
        assert len(dataList) == 5
        assert len(dataList[0].data()) == 1
        assert dataList[0].data()[0] == 0
        assert dataList[1].data()[0] == 1.0
        assert dataList[2].data()[0] == 2.0
        assert dataList[3].data()[0] == 3.0
        assert dataList[4].data()[0] == 4.0
        

    def test_parseDataLine_MultipleDataLine(self):
        parser = DataParser()

        dataList = []
        inputLine = "0;1.0;2.0;3.0;4.0;"
        parser.parseDataLine(inputLine, dataList)
        inputLine = "1;1.1;2.0;3.0;4.0;"
        parser.parseDataLine(inputLine, dataList)
        inputLine = "2;1.2;2.0;3.0;4.0;"
        parser.parseDataLine(inputLine, dataList)
        inputLine = "3;1.3;2.0;3.0;4.0;"
        parser.parseDataLine(inputLine, dataList)
        assert parser.unit() == "s"
        assert parser.unitValue() == 1
        assert len(dataList) == 5
        assert len(dataList[0].data()) == 4
        assert dataList[0].data()[3] == 3


    def test_splitLineToValueList(self):
        parser = DataParser()

        valueList = []
        
        inputLine = "4378,0;343,43;3434,0;34,0;"
        valueList = parser.splitLineToValueList(inputLine, ";")
        assert len(valueList) == 4
        assert valueList == ['4378,0', '343,43', '3434,0', '34,0']

    def test_checkAndReplaceComma(self):
        parser = DataParser()

        valueText = "4343,9"
        valueText = parser.checkAndReplaceComma(valueText)
        assert valueText == "4343.9"



if __name__ == '__main__': 
    test = TestDataParser()
    test.test_parseDataLine_MultipleDataLine()


    

                 