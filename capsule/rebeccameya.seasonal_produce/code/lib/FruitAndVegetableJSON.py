import json

produce = '''
[
    { "name" : "Apples",
    "type" : "Fruit",
    "season" : ["Spring", "Summer", "Fall", "Winter"]
    },
    { "name" : "Apricots",
    "type" : "Fruit",
    "season" : ["Spring", "Summer"]
    }, 
    { "name" : "Bananas",
    "type" : "Fruit",
    "season" : ["Spring", "Summer", "Fall", "Winter"]
    },
    { "name" : "Blackberries",
    "type" : "Fruit",
    "season" : "Summer"
    },
    { "name" : "Blueberries",
    "type" : "Fruit",
    "season" : "Summer"
    },
    { "name" : "Cantaloupe",
    "type" : "Fruit",
    "season" : "Summer"
    },
    { "name" : "Cherries",
    "type" : "Fruit",
    "season" : "Summer"
    },
    { "name" : "Cranberries",
    "type" : "Fruit",
    "season" : "Fall"
    },
    { "name" : "Grapefruit",
    "type" : "Fruit",
    "season" : "Winter"
    },
    { "name" : "Grapes",
    "type" : "Fruit",
    "season" : "Fall"
    },
    { "name" : "Honeydew Melon",
    "type" : "Fruit",
    "season" : "Summer"
    },
    { "name" : "Kiwis",
    "type" : "Fruit",
    "season" : ["Spring", "Fall", "Winter"]
    },
    { "name" : "Lemons",
    "type" : "Fruit",
    "season" : ["Spring", "Summer", "Fall", "Winter"]
    },
    { "name" : "Limes",
    "type" : "Fruit",
    "season" : ["Spring", "Summer", "Fall", "Winter"]
    },
    { "name" : "Mangos",
    "type" : "Fruit",
    "season" : ["Summer", "Fall"]
    },
    { "name" : "Oranges",
    "type" : "Fruit",
    "season" : "Winter"
    },
    { "name" : "Peaches",
    "type" : "Fruit",
    "season" : "Summer"
    },
    { "name" : "Pears",
    "type" : "Fruit",
    "season" : ["Fall", "Winter"]
    },
    { "name" : "Pineapples",
    "type" : "Fruit",
    "season" : ["Spring", "Fall", "Winter"]
    },
    { "name" : "Plums",
    "type" : "Fruit",
    "season" : "Summer"
    },
    { "name" : "Raspberries",
    "type" : "Fruit",
    "season" : ["Summer", "Fall"]
    },
    { "name" : "Strawberries",
    "type" : "Fruit",
    "season" : ["Spring", "Summer"]
    },
    { "name" : "Watermelon",
    "type" : "Fruit",
    "season" : "Summer"
    },
    { "name" : "Asparagus",
    "type" : "Vegetable",
    "season" : "Spring"
    },
    { "name" : "Avocados",
    "type" : "Vegetable",
    "season" : ["Spring", "Summer", "Winter"]
    },
    { "name" : "Beets",
    "type" : "Vegetable",
    "season" : ["Summer", "Fall", "Winter"]
    },
    { "name" : "Bell Peppers",
    "type" : "Vegetable",
    "season" : ["Summer", "Fall"]
    },
    { "name" : "Broccoli",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall"]
    },
    { "name" : "Brussel Sprouts",
    "type" : "Vegetable",
    "season" : ["Fall", "Winter"]
    },
    { "name" : "Cabbage",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall", "Winter"]
    },
    { "name" : "Carrots",
    "type" : "Vegetable",
    "season" : ["Spring", "Summer", "Fall", "Winter"]
    },
    { "name" : "Cauliflower",
    "type" : "Vegetable",
    "season" : "Fall"
    },
    { "name" : "Celery",
    "type" : "Vegetable",
    "season" : ["Spring", "Summer", "Fall", "Winter"]
    },
    { "name" : "Collard Greens",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall", "Winter"]
    },
    { "name" : "Corn",
    "type" : "Vegetable",
    "season" : "Summer"
    },
    { "name" : "Cucumbers",
    "type" : "Vegetable",
    "season" : "Summer"
    },
    { "name" : "Eggplant",
    "type" : "Vegetable",
    "season" : "Summer"
    },
    { "name" : "Garlic",
    "type" : "Vegetable",
    "season" : ["Spring", "Summer", "Fall"]
    },
    { "name" : "Ginger",
    "type" : "Vegetable",
    "season" : "Fall"
    },
    { "name" : "Green Beans",
    "type" : "Vegetable",
    "season" : ["Summer", "Fall"]
    },
    { "name" : "Herbs",
    "type" : "Vegetable",
    "season" : ["Spring", "Summer", "Fall", "Winter"]
    },
    { "name" : "Kale",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall", "Winter"]
    },
    { "name" : "Leeks",
    "type" : "Vegetable",
    "season" : "Winter"
    },
    { "name" : "Lettuce",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall"]
    },
    { "name" : "Lima Beans",
    "type" : "Vegetable",
    "season" : "Summer"
    },
    { "name" : "Mushrooms",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall"]
    },
    { "name" : "Okra",
    "type" : "Vegetable",
    "season" : "Summer"
    },
    { "name" : "Onions",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall", "Winter"]
    },
    { "name" : "Parsnips",
    "type" : "Vegetable",
    "season" : ["Fall", "Winter"]
    },
    { "name" : "Peas",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall"]
    },
    { "name" : "Potatoes",
    "type" : "Vegetable",
    "season" : ["Fall", "Winter"]
    },
    { "name" : "Pumpkin",
    "type" : "Vegetable",
    "season" : ["Fall", "Winter"]
    },
    { "name" : "Radishes",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall"]
    },
    { "name" : "Rhubarb",
    "type" : "Vegetable",
    "season" : "Spring"
    },
    { "name" : "Rutabagas",
    "type" : "Vegetable",
    "season" : ["Fall", "Winter"]
    },
    { "name" : "Spinach",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall"]
    },
    { "name" : "Summer Squash",
    "type" : "Vegetable",
    "season" : "Summer"
    },
    { "name" : "Sweet Potatoes",
    "type" : "Vegetable",
    "season" : ["Fall", "Winter"]
    },
    { "name" : "Swiss Chard",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall", "Winter"]
    },
    { "name" : "Tomatillos",
    "type" : "Vegetable",
    "season" : "Summer"
    },
    { "name" : "Tomatoes",
    "type" : "Vegetable",
    "season" : "Summer"
    },
    { "name" : "Turnips",
    "type" : "Vegetable",
    "season" : ["Spring", "Fall", "Winter"]
    },
    { "name" : "Winter Squash",
    "type" : "Vegetable",
    "season" : ["Fall", "Winter"]
    },
    { "name" : "Zucchini",
    "type" : "Vegetable",
    "season" : "Summer"
    }
]
'''