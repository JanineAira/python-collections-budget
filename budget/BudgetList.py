class BudgetList:
    def __init__(self, budget):
        self.budget = budget
        self.sum_expense = 0
        self.expenses = []
        self.sum_overages = 0

        def append(self, item):
            if (self.sum_expenses + item) < self.budget:
                self.expenses.append(item)
                self.sum_expenses += item