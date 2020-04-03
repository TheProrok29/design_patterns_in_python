class Computer:
    """Example computer"""

    def __init__(self, processor):
        """Initialize instance"""
        self.processor = processor  # Processor is  injected

    def __str__(self):
        return f'I have {self.processor} processor!'
