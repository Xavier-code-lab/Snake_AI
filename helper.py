import matplotlib.pyplot as plt
import time

# Ensure this is the first line in the script to initialize interactive mode
plt.ion()

def plot(scores, mean_scores):
    plt.clf()  # Clear the previous plot
    plt.figure(figsize=(12, 6))  # Make the figure larger
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    
    plt.pause(0.1)  # Pause to allow the plot to update (no new window)

