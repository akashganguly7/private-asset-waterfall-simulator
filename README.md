# 💧 Private Equity Waterfall Simulator

A Streamlit web application that simulates and visualizes the distribution of profits in a private equity fund using the standard waterfall structure. This tool helps Limited Partners (LPs) and General Partners (GPs) understand how exit proceeds are allocated according to fund terms.

## Features

- **Interactive Waterfall Calculation**: Calculate profit distribution based on customizable parameters
- **Visual Waterfall Chart**: Interactive Plotly visualization showing the distribution flow
- **Step-by-Step Breakdown**: Detailed table showing each stage of the waterfall
- **Real-time Calculations**: Adjust parameters and see results instantly

## Waterfall Structure

The simulator follows the standard private equity waterfall model:

1. **LP Capital Return**: Return of the original capital invested by Limited Partners
2. **LP Preferred Return**: Payment of preferred return (hurdle rate) to LPs
3. **GP Catch-Up**: General Partner catch-up to achieve target carry percentage
4. **Final Split**: Remaining proceeds split between LP (80%) and GP (20%)

## Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd private-asset-waterfall-simulator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. The application will open in your default web browser.

3. Adjust the parameters in the sidebar:
   - **LP Capital Invested**: Initial capital invested by Limited Partners (€)
   - **Exit Value**: Total exit value/proceeds (€)
   - **Years Invested**: Investment holding period
   - **Preferred Return (Hurdle %)**: Annual preferred return rate (typically 8%)
   - **GP Carry %**: General Partner carried interest percentage (typically 20%)

4. Click **"Calculate Waterfall"** to see the distribution breakdown and visualization.

## Project Structure

```
private-asset-waterfall-simulator/
├── app.py              # Main Streamlit application
├── waterfall.py        # Waterfall calculation functions
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── venv/              # Virtual environment (not in git)
```

## Dependencies

- `streamlit`: Web application framework
- `plotly`: Interactive charting library
- `pandas`: Data manipulation
- `numpy`: Numerical computations

## How It Works

The waterfall calculation follows these steps:

1. **Return Capital**: First, return the original LP capital investment
2. **Preferred Return**: Calculate and pay preferred return based on hurdle rate and years invested
3. **GP Catch-Up**: Allocate funds to GP until they reach their target carry percentage
4. **Final Split**: Distribute remaining proceeds 80% to LP and 20% to GP

## Example

**Input:**
- LP Capital Invested: €5,000
- Exit Value: €10,000
- Years Invested: 5
- Preferred Return: 8%
- GP Carry: 20%

**Result:**
- Total Profit: €5,000
- LP receives: Capital return + Preferred return + 80% of remaining
- GP receives: Catch-up + 20% of remaining

## License

This project is open source and available for educational and commercial use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

