import Process


class OrderedArrayRQ:
    def __init__(self):
        self.queue = []

    def enqueue(self, procLabel, vt):
        for i in len(self.queue):
            if (vt < self.queue[i].vt):
                self.queue.insert(i, Process(procLabel, vt))

    def dequeue(self):
        if len(self.queue) > 0:
            procLabel = self.queue[0].procLabel
            self.queue.pop[0]
            return procLabel
        return ''

    def findProcess(self, procLabel):
        for process in self.queue:
            if (process.proLabel == procLabel):
                return True
        return False

    def removeProcess(self, procLabel):
        for process in self.queue:
            if (process.proLabel == procLabel):
                self.queue.remove(process)
                return True
        return False

    def succedingProcessTime(self, procLabel):
        for i in len(self.queue):
            if (self.queue[i].proLabel == procLabel):
                processTime = 0
                startIndex = i + 1
                processAmount = len(self.queue) - startIndex
                for j in processAmount:
                    processTime += self.queue[j+startIndex]
                return processTime
        return -1

    def printAllProcesses(self):
        if len(self.queue) > 0:
            for process in self.queue:
                print(process.procLabel)
        return ''
