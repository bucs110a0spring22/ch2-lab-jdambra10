import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 2
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class))
print("Cost per class:", cost_per_class)

#Part B
#Random Agent generator for who to pick 
valorant_agents = ["Cypher", "Killjoy", "Sage", "Chamber", "Viper", "Brimstone", "Astra", "Omen", "Sova", "Breach", "KAY/O", "Skye", "Phoenix", "Jett", "Reyna", "Raze", "Neon", "Yoru"]

chosen_agent = random.choice(valorant_agents)
print("For your next game, you should pick:", chosen_agent)
