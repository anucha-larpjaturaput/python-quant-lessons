from rich.console import Console
import numpy as np

console = Console()

# Generate fake XAU/USD prices
prices = np.array([2370, 2375, 2382, 2376, 2390, 2405, 2412, 2408, 2418, 2425], dtype=float)

# Compute daily returns (% change)
returns = (prices[1:] - prices[:-1]) / prices[:-1] * 100

# Compute simple moving average (SMA)
def simple_moving_average(data, window):
    return np.convolve(data, np.ones(window)/window, mode='valid')

sma_3 = simple_moving_average(prices, 3)
signals = prices[2:] > sma_3

console.rule("[bold yellow]Quant Lesson 1 — NumPy Basics[/bold yellow]")
console.print(f"[cyan]Prices:[/cyan] {prices}")
console.print(f"[magenta]Daily returns (%):[/magenta] {np.round(returns, 3)}")
console.print(f"[green]3-day SMA:[/green] {np.round(sma_3, 2)}")
console.print(f"[bold blue]Signals (True=Buy):[/bold blue] {signals}")
console.rule()
