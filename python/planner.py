# 'Planner' class hierarchy
class Planner:
    def __init__(self, month, year, startDate, endDate, startWeekDay="Mon", myPlanner=[]):
        self.myPlanner = myPlanner #data structure to hold Page objects
        self.month = month
        self.year = year
        self.startDate = startDate
        self.endDate = endDate
        self.startWeekDay = startWeekDay

        #Set section variable of page objects
        self.setSections()

    #TODO
    def addPage(self):
        """ Initialize new Page object & add it to the end of myPlanner """

    def setSections(self):
        """ Assign printed page orientation to each page based on list order """
        if len(self.myPlanner) % 2 == 0:
            for index in range(int(len(self.myPlanner)/4)):
                self.myPlanner[4*index].setSection("left_front")
                self.myPlanner[4*index+1].setSection("right_front")
                self.myPlanner[4*index+2].setSection("left_back")
                self.myPlanner[4*index+3].setSection("right_back")
        else:
            print("Booklet must be size divisible by 2")

    def getPrinterSpread(self):
        """ Return Page objects ordered by printer spread """
        print_order = []
        frontPointer = 0
        backPointer = len(self.myPlanner) - 1
        if len(self.myPlanner) % 2 == 0:
            print_order.append(self.myPlanner[backPointer]) #pop back
            backPointer = backPointer - 1 #update pointer
            front = True
            for num in range(int((len(self.myPlanner)-2)/2)):
                if front == True:
                    print_order.append(self.myPlanner[frontPointer]) #pop front
                    frontPointer = frontPointer + 1 #update pointer
                    print_order.append(self.myPlanner[frontPointer]) #pop front
                    frontPointer = frontPointer + 1 #update pointer
                    front = not front
                elif front == False:
                    print_order.append(self.myPlanner[backPointer]) #pop back
                    backPointer = backPointer - 1 #update pointer
                    print_order.append(self.myPlanner[backPointer]) #pop back
                    backPointer = backPointer - 1 #update pointer
                    front = not front
            print_order.append(self.myPlanner[frontPointer]) #pop final page
            return print_order
        else:
            print("booklet must be size divisible by 2")

    def getReaderSpread(self):
        """ Return Page objects ordered by reader spread """
        return self.myPlanner

    def createPlanner(self, filename='out.html', size='5x8'):
        """ Run createPage() for all Pages in Planner, writes HTML file to out folder """
        printPlanner = self.getPrinterSpread()

        f = open(f'./out/{filename}', 'w', encoding='utf-8')
    
        # html head
        fhead = open(f'./page_html/{size}/head.html', 'r', encoding='utf-8')
        for line in fhead:
            f.write(line)

        # html body
        f.write("""
        <!-- Content of the booklet -->
        <body>""")
            
        for index in range(int(len(printPlanner)/4)):

            #page1
            f.write("""
            
            <div class="page">
    """)
            f.write(printPlanner[4*index].createPage(size))

            #page2
            f.write(printPlanner[4*index+1].createPage(size))
            f.write("""
                </div>
    """)

            #page3
            f.write("""
            
            <div class="page">
    """)
            f.write(printPlanner[4*index+2].createPage(size))

            #page4
            f.write(printPlanner[4*index+3].createPage(size))
            f.write("""
            </div>
            """)
                
        f.write("""
        
        </body>
                """)
    
        f.close()