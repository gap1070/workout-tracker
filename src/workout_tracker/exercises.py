"""Exercise classes for the workout tracker."""

from datetime import datetime


class Exercise:
    """Base class for all exercise types.
    
    Attributes:
        name (str): The name of the exercise
        date (str): The date the exercise was performed (YYYY-MM-DD format)
    """
    
    def __init__(self, name: str, date: str = None):
        """Initialize an Exercise.
        
        Args:
            name: The name of the exercise
            date: The date performed (defaults to today if not provided)
        """
        self.name = name
        if date is None: 
            self.date = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date = date
    
    def calculate_calories(self) -> float:
        """Calculate calories burned for this exercise.
        
        Subclasses must override this method.
        
        Returns:
            float: Estimated calories burned
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def get_duration(self) -> float:
        """Get the duration of the exercise in minutes.
        
        Subclasses must override this method.
        
        Returns:
            float: Duration in minutes
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def __str__(self) -> str:
        """Return a string representation of the exercise."""
        return f"{self.name}: {self.calculate_calories()} calories"
    

class CardioExercise(Exercise):
    """Cardio exercise with distance and time tracking.
    
    Attributes:
        name (str): Exercise name
        date (str): Date performed
        distance (float): Distance covered in miles
        duration (float): Time spent in minutes
    """
    
    def __init__(self, name: str, distance: float, duration: float, date: str = None):
        """Initialize a CardioExercise.
        
        Args:
            name: Exercise name (e.g., "Running", "Cycling")
            distance: Distance covered in miles
            duration: Time spent in minutes
            date: Date performed (optional)
        """
        super().__init__(name, date)
        self.distance = distance 
        self.duration = duration 
    
    def calculate_calories(self) -> float:
        """Calculate calories burned based on distance.
        
        Formula: distance * 100
        
        Returns:
            float: Estimated calories burned
        """
        return self.distance * 100 
    
    def get_duration(self) -> float:
        """Get the duration of the cardio exercise.
        
        Returns:
            float: Duration in minutes
        """
        return self.duration
    
    def __str__(self) -> str:
        """Return detailed string representation."""
        return f"{self.name} ({self.distance} miles, {self.duration} min): {self.calculate_calories()} calories"
    

class StrengthExercise(Exercise):
    """This class will track weight, reps, and sets
    
    Attributes:
        name (str): Exercise name
        date (str): Date performed
        weight( (float): Pounds lifted
        reps (int): Repititions per set
        sets (int): Number of sets 
    """

    def __init__(self, name: str, weight: float, reps: int, sets: int, date: str = None):
        # calls the parent function 
        super().__init__(name, date)

        # stores all the information for the different attributes 
        self.weight = weight
        self.reps = reps
        self.sets = sets 

    def calculate_calories(self) -> float:
        """Calculates your calories burned with a certain formula"""
        return self.weight * self.reps * self.sets * 0.05
    
    def get_duration(self) -> float:
        """Gets the duration of your exercise using a certain formula"""
        return self.sets * 3
    
    def __str__(self) -> str:
        """Returns the details of your workout in a string"""
        calories = self.calculate_calories()
        return (
            f"{self.name} ({self.weight} lbs x {self.reps} reps x "
            f"{self.sets} sets): {calories:.0f} calories"
        )