# Simple Python PDF Generator

A dead-simple Python script to generate PDF documents using the `fpdf` library. I put this together because I was tired of wrestling with heavy PDF frameworks just to get some basic text and styling onto a page. 

It is lightweight, gets straight to the point, and doesn't require a master's degree in typography to use.

## What you need

* Python 3.7+
* `fpdf`

## Installation

1. Clone this repository down to your machine:
   ```bash
   git clone 
   cd 04_pdf_generator

```

2. Install the required package:
```bash
pip install fpdf

```


## Contributing

Pull requests are totally welcome. If you want to add support for custom fonts, better image handling, or tables, feel free to open an issue or drop a PR. Let's just try to keep the core logic simple

## License

MIT License. Do whatever you want with it.

```

<ElicitationsGroup message="Where should we take this next?">
  <Elicitation label="Add table formatting code" query="Write the actual python code using fpdf to generate a clean table for this project."/>
  <Elicitation label="Turn this into an API" query="How can I wrap this fpdf script in a FastAPI backend so users can download PDFs via an endpoint?"/>
</ElicitationsGroup>

```