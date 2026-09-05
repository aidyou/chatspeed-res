---
title: "calculator"
description: "MCP Calculator Server A full-featured Model Context Protocol (MCP) calculator server offering a rich set of mathematical operations across 13 specialized modules: basic arithmetic, roots, trigonometry…"
---

# calculator

MCP Calculator Server A full-featured Model Context Protocol (MCP) calculator server offering a rich set of mathematical operations across 13 specialized modules: basic arithmetic, roots, trigonometry…

# MCP Calculator Server

[![npm version](/mcp-assets/8e7cef31ffd2a60eb8a10d31be875b35.svg)](https://badge.fury.io/js/mcp-calculator)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](/mcp-assets/e2f4f7eb3c57946e147a6d1fb44ccbbc.svg)](https://www.typescriptlang.org/)
[![Node.js](/mcp-assets/6cb98474e7605f1c68a4efc113f8119a.svg)](https://nodejs.org/)

A full-featured Model Context Protocol (MCP) calculator server offering a rich set of mathematical operations across 13 specialized modules: basic arithmetic, roots, trigonometry, logarithms, statistics, combinatorics, number theory, complex numbers, matrix operations, numerical analysis, financial calculations, unit conversions, and geometry.

## Installation

### Via npm (recommended)

```bash
# Global install
npm install -g mcp-calculator

# Or local install
npm install mcp-calculator
```

### From source

```bash
# Clone the project
git clone https://github.com/proflulab/mcp-calculator.git
cd mcp-calculator

# Install dependencies
npm install

# Build and start
npm start
```

## Quick Start

### After global install

```bash
# Start the server directly
calculator
```

### After local install

```bash
# Run with npx
npx mcp-calculator

# Or via npm scripts
npm start
```

## Features

### 13 Specialized Math Modules

#### 1. Basic Math

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers (including division-by-zero error handling)
- Modulo: remainder of two numbers
- Exponentiation: a raised to the power of b

#### 2. Root Operations

- Square root
- Cube root
- n-th root of a number
- Absolute value

#### 3. Trigonometry

- Basic trigonometric functions: sin, cos, tan
- Inverse trigonometric functions: asin, acos, atan
- Hyperbolic functions: sinh, cosh, tanh
- Degree/radian conversion

#### 4. Logarithms

- Natural logarithm: ln(x)
- Common logarithm: log10(x)
- Logarithm with arbitrary base: log_b(x)
- Exponential functions: e^x, 10^x, a^x

#### 5. Statistics

- Descriptive statistics: mean, median, mode
- Dispersion measures: standard deviation, variance, range
- Extremes: max, min
- Aggregations: sum, product

#### 6. Combinatorics

- Factorial: n!
- Permutations and combinations: P(n,r), C(n,r)
- Fibonacci sequence: n-th Fibonacci number
- Catalan numbers: n-th Catalan number

#### 7. Number Theory

- Greatest common divisor (GCD)
- Least common multiple (LCM)
- Primality test
- Prime factorization
- Euler's totient function: phi(n)
- Perfect number detection
- Divisor count and list

#### 8. Complex Numbers

- Basic operations: add, subtract, multiply, divide
- Complex properties: magnitude, conjugate, argument
- Polar form: r phase angle representation

#### 9. Matrix Operations

- Matrix arithmetic: addition, subtraction, multiplication
- Matrix properties: determinant, transpose, inverse
- Vector operations: dot product, cross product, magnitude

#### 10. Numerical Analysis

- Numerical integration: trapezoidal rule, Simpson's rule
- Numerical differentiation
- Root finding: Newton's method, bisection method
- Interpolation: Lagrange interpolation

#### 11. Financial

- Compound interest: investment returns
- Annuities: present and future value
- Loans: monthly payment calculation
- Investment analysis: NPV, IRR
- Bond pricing

#### 12. Conversions

- Length: meters, feet, inches, etc.
- Weight: kilograms, pounds, ounces, etc.
- Temperature: Celsius, Fahrenheit, Kelvin
- Area and volume: conversions between units
- Time: seconds, minutes, hours, etc.

#### 13. Geometry

- Plane geometry: circle, rectangle, triangle area and perimeter
- Solid geometry: sphere, cylinder, cone volume and surface area
- Coordinate geometry: point distance, line equations

### System Features

- Parameter validation with Zod
- Comprehensive error handling
- Modular design: 13 independent math modules
- Type safety: complete TypeScript type definitions
- Unit tests: 266 test cases, 100% coverage

## Installation and Usage

### 1. Install dependencies

```bash
npm install
```

### 2. Build the project

```bash
npm run build
```

### 3. Start the server

```bash
npm start
```

Or run the built file directly:

```bash
node build/index.js
```

### 4. Test the server

For detailed testing instructions and usage, see the [test docs](https://github.com/proflulab/mcp-calculator/blob/HEAD/tests/README.md).

Quick test commands:

```bash
# Run all tests
npm test

# Run unit tests
npm run test:unit

# Run integration tests
npm run test:integration

# Generate coverage report
npm run test:coverage
```

## Usage Examples

### In an MCP client

#### Global install configuration

If you installed `mcp-calculator` globally:

```json
{
  "mcpServers": {
    "calculator": {
      "command": "calculator"
    }
  }
}
```

#### Local install configuration

For a local install or built from source:

```json
{
  "mcpServers": {
    "calculator": {
      "command": "node",
      "args": ["/path/to/mcp_calculator/build/index.js"]
    }
  }
}
```

#### Using npx

```json
{
  "mcpServers": {
    "calculator": {
      "command": "npx",
      "args": ["mcp-calculator"]
    }
  }
}
```

### Calculator examples

- **Basic operations**: "compute 15 + 27"
- **Trigonometry**: "compute sin(pi/4)"
- **Logarithms**: "compute log2(16)"
- **Roots**: "compute cube root of 125"
- **Compound expressions**: "compute 2^3 + sqrt(16) - ln(e)"

### Using the CLI directly

```bash
# Start the server
node build/index.js

# Send a request from another terminal
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"add","arguments":{"a":10,"b":5}}}' | node build/index.js
```

### Verify installation

```bash
# Check the version
npm list mcp-calculator

# Run tests (if installed from source)
npm run test:all

# Start a server test
calculator  # global install
# or
npx mcp-calculator  # local install
```

## Available Tools

This project provides **100+** math tools organized into 13 specialized modules. Here are the main tools in each module:

### 1. Basic Math

| Tool | Description | Example |
|--------|------|--------|
| `add` | Addition | `add(10, 5) = 15` |
| `subtract` | Subtraction | `subtract(10, 5) = 5` |
| `multiply` | Multiplication | `multiply(10, 5) = 50` |
| `divide` | Division | `divide(10, 5) = 2` |
| `modulo` | Modulo | `modulo(17, 5) = 2` |
| `power` | Exponentiation | `power(2, 8) = 256` |

### 2. Root Operations

| Tool | Description | Example |
|--------|------|------|
| `sqrt` | Square root | `sqrt(16) = 4` |
| `cbrt` | Cube root | `cbrt(27) = 3` |
| `nthRoot` | n-th root | `nthRoot(16, 4) = 2` |
| `abs` | Absolute value | `abs(-25) = 25` |

### 3. Trigonometry

| Tool | Description | Example |
|--------|------|------|
| `sin` | Sine | `sin(pi/2) = 1` |
| `cos` | Cosine | `cos(0) = 1` |
| `tan` | Tangent | `tan(pi/4) = 1` |
| `asin` | Arc sine | `asin(0.5) = pi/6` |
| `acos` | Arc cosine | `acos(0.5) = pi/3` |
| `atan` | Arc tangent | `atan(1) = pi/4` |
| `sinh` | Hyperbolic sine | `sinh(0) = 0` |
| `degrees_to_radians` | Degrees to radians | `degrees_to_radians(180) = pi` |

### 4. Logarithms

| Tool | Description | Example |
|--------|------|------|
| `ln` | Natural logarithm | `ln(e) = 1` |
| `log10` | Common logarithm | `log10(100) = 2` |
| `log` | Arbitrary-base logarithm | `log(8, 2) = 3` |
| `exp` | Exponential function | `exp(1) = e` |

### 5. Statistics

| Tool | Description | Example |
|--------|------|------|
| `mean` | Mean | `mean([1,2,3,4,5]) = 3` |
| `median` | Median | `median([1,2,3,4,5]) = 3` |
| `mode` | Mode | `mode([1,1,2,3]) = 1` |
| `stdDev` | Standard deviation | `stdDev([1,2,3,4,5]) = 1.58` |
| `variance` | Variance | `variance([1,2,3,4,5]) = 2.5` |
| `max` | Maximum | `max([1,2,3,4,5]) = 5` |
| `min` | Minimum | `min([1,2,3,4,5]) = 1` |
| `sum` | Sum | `sum([1,2,3,4,5]) = 15` |
| `product` | Product | `product([1,2,3,4,5]) = 120` |
| `range` | Range | `range([1,2,3,4,5]) = 4` |

### 6. Combinatorics

| Tool | Description | Example |
|--------|------|------|
| `factorial` | Factorial | `factorial(5) = 120` |
| `permutation` | Permutation | `permutation(5, 3) = 60` |
| `combination` | Combination | `combination(5, 3) = 10` |
| `fibonacci` | Fibonacci | `fibonacci(10) = 55` |

### 7. Number Theory

| Tool | Description | Example |
|--------|------|------|
| `gcd` | Greatest common divisor | `gcd(12, 18) = 6` |
| `lcm` | Least common multiple | `lcm(12, 18) = 36` |
| `isPrime` | Primality test | `isPrime(17) = true` |
| `primeFactorization` | Prime factorization | `primeFactorization(12) = [2,2,3]` |
| `eulerTotient` | Euler's totient | `eulerTotient(9) = 6` |
| `isPerfectNumber` | Perfect number | `isPerfectNumber(6) = true` |
| `divisorCount` | Divisor count | `divisorCount(12) = 6` |
| `divisorList` | Divisor list | `divisorList(12) = [1,2,3,4,6,12]` |

### 8. Complex Numbers

| Tool | Description | Example |
|--------|------|------|
| `complex_add` | Complex addition | `(3+4i) + (1+2i) = 4+6i` |
| `complex_subtract` | Complex subtraction | `(3+4i) - (1+2i) = 2+2i` |
| `complex_multiply` | Complex multiplication | `(3+4i) * (1+2i) = -5+10i` |
| `complex_divide` | Complex division | `(3+4i) / (1+2i) = 2.2-0.4i` |
| `complex_magnitude` | Complex magnitude | `\|3+4i\| = 5` |
| `complex_conjugate` | Complex conjugate | `conj(3+4i) = 3-4i` |
| `complex_argument` | Complex argument | `arg(3+4i) = 0.927` |
| `complex_polar` | Polar form | `3+4i = 5 angle 0.927` |

### 9. Matrix Operations

| Tool | Description | Example |
|--------|------|------|
| `matrix_add` | Matrix addition | `[[1,2],[3,4]] + [[5,6],[7,8]]` |
| `matrix_subtract` | Matrix subtraction | `[[1,2],[3,4]] - [[5,6],[7,8]]` |
| `matrix_multiply` | Matrix multiplication | `[[1,2],[3,4]] x [[5,6],[7,8]]` |
| `matrix_determinant` | Determinant | `det([[1,2],[3,4]]) = -2` |
| `matrix_transpose` | Transpose | `transpose([[1,2],[3,4]])` |
| `vector_dot_product` | Vector dot product | `[1,2,3] . [4,5,6] = 32` |
| `vector_magnitude` | Vector magnitude | `\|[3,4]\| = 5` |

### 10. Numerical Analysis

| Tool | Description | Example |
|--------|------|------|
| `numerical_integration` | Numerical integration | Trapezoidal and Simpson's rules |
| `numerical_derivative` | Numerical differentiation | Numerical derivative |
| `newton_method` | Newton's method | Root finding |
| `bisection_method` | Bisection method | Root finding |
| `lagrange_interpolation` | Lagrange interpolation | Interpolation |

### 11. Financial

| Tool | Description | Example |
|--------|------|------|
| `compound_interest` | Compound interest | Investment return |
| `present_value_annuity` | Annuity present value | Present value of an annuity |
| `future_value_annuity` | Annuity future value | Future value of an annuity |
| `loan_payment` | Loan payment | Equal monthly installments |
| `net_present_value` | Net present value | NPV |
| `internal_rate_of_return` | Internal rate of return | IRR |
| `bond_price` | Bond price | Bond pricing |

### 12. Conversions

| Tool | Description | Example |
|--------|------|------|
| `length_conversion` | Length conversion | meters, feet, inches |
| `weight_conversion` | Weight conversion | kilograms, pounds, ounces |
| `temperature_conversion` | Temperature conversion | Celsius, Fahrenheit, Kelvin |
| `area_conversion` | Area conversion | square meters, acres, etc. |
| `time_conversion` | Time conversion | seconds, minutes, hours, etc. |

### 13. Geometry

| Tool | Description | Example |
|--------|------|------|
| `circle_area` | Circle area | `pi * r^2` |
| `rectangle_area` | Rectangle area | `length * width` |
| `triangle_area` | Triangle area | `1/2 * base * height` |
| `sphere_volume` | Sphere volume | `4/3 * pi * r^3` |
| `cylinder_volume` | Cylinder volume | `pi * r^2 * h` |
| `distance_between_points` | Point distance | Distance between two points |

> **Tip**: Every tool includes full parameter validation, error handling, and detailed usage instructions. Use the `tools/list` method of the MCP protocol to get the complete definitions of all tools.

## MCP Protocol Usage

### Connecting to the server

The server communicates over standard input/output (stdio) and supports the JSON-RPC 2.0 protocol.

### Listing tools

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list"
}
```

## Tech Stack

- **TypeScript**: main development language, providing type safety
- **@modelcontextprotocol/sdk**: MCP protocol implementation
- **Zod**: runtime type validation and input checking
- **Node.js**: runtime environment

### Dependency versions

- Node.js >= 16.0.0
- TypeScript >= 5.0.0
- @modelcontextprotocol/sdk ^1.17.4
- Zod ^3.25.76

## Project Structure

```text
mcp-calculator/
├── src/                      # Source directory
│   ├── index.ts              # Main server file
│   ├── types.ts              # Type definitions
│   └── modules/              # Math modules
│       ├── basicMath.ts      # Basic math
│       ├── rootOperations.ts # Root operations
│       ├── trigonometry.ts   # Trigonometry
│       ├── logarithm.ts      # Logarithms
│       ├── statistics.ts     # Statistics
│       ├── combinatorics.ts  # Combinatorics
│       ├── numberTheory.ts   # Number theory
│       ├── complex.ts        # Complex numbers
│       ├── matrix.ts         # Matrices
│       ├── numerical.ts      # Numerical analysis
│       ├── financial.ts      # Financial math
│       ├── conversion.ts     # Unit conversions
│       └── geometry.ts       # Geometry
├── tests/                    # Tests
│   ├── unit/                 # Unit tests
│   │   ├── basicMath.test.ts
│   │   ├── rootOperations.test.ts
│   │   ├── trigonometry.test.ts
│   │   ├── logarithm.test.ts
│   │   ├── statistics.test.ts
│   │   ├── combinatorics.test.ts
│   │   ├── numberTheory.test.ts
│   │   ├── complex.test.ts
│   │   ├── matrix.test.ts
│   │   ├── numerical.test.ts
│   │   ├── financial.test.ts
│   │   ├── conversion.test.ts
│   │   └── geometry.test.ts
│   ├── integration/           # Integration tests
│   ├── performance/          # Performance tests
│   ├── jest.config.cjs       # Jest config
│   ├── setup.ts              # Test environment setup
│   ├── coverage/             # Coverage reports
│   └── README.md             # Test documentation
├── build/                    # Compiled output
├── package.json              # Project config and dependencies
├── package-lock.json         # Locked dependency versions
├── tsconfig.json             # TypeScript config
├── .gitignore                # Git ignore rules
├── LICENSE                   # MIT license
└── README.md                 # Project readme
```

## Development Scripts

### Build and run

- `npm run build` - compile TypeScript
- `npm start` - build and start the server
- `npm run dev` - development mode (auto-recompile on file changes)

## Contributing

Issues and Pull Requests are welcome!

### Development flow

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code standards

- Develop in TypeScript
- Follow existing code style
- Add tests for new features
- Update documentation

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/proflulab/mcp-calculator/blob/HEAD/LICENSE) file for details.

## Version Info

Current version: **v1.0.1**

### Changelog

- **v1.0.1** - Initial release
  - Supports 19 math operation tools
  - Complete error handling
  - 100% test coverage
  - Published to npm

## Related Links

- **npm package**: [mcp-calculator](https://www.npmjs.com/package/mcp-calculator)
- **GitHub repository**: [mcp-calculator](https://github.com/your-username/mcp-calculator)
- [Model Context Protocol docs](https://modelcontextprotocol.io/)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Zod validation library](https://github.com/colinhacks/zod)

## Feature Statistics

- **100+** math tools
- **13** specialized math modules
- **266** test cases
- **14** test suites
- **100%** test coverage
- **100%** test pass rate
- **Complete** error handling
- **TypeScript** type safety
- **Modular** architecture

## Performance Features

- **Lightweight**: small compiled size, fast startup
- **Memory efficient**: low memory footprint, suitable for long-running processes
- **Type safe**: complete TypeScript type definitions
- **Error recovery**: a single calculation error does not affect the server

## API Reference

### Modules

| Module | Tools | Main functions |
|------|----------|----------|
| Basic Math | 6 | add, subtract, multiply, divide, modulo, power |
| Root Operations | 4 | square root, cube root, n-th root, absolute value |
| Trigonometry | 8 | basic trig, inverse trig, hyperbolic functions |
| Logarithms | 4 | natural log, common log, arbitrary-base log, exponentials |
| Statistics | 10 | mean, median, standard deviation, variance, etc. |
| Combinatorics | 4 | factorial, permutations, combinations, Fibonacci, Catalan |
| Number Theory | 8 | GCD, LCM, primality, factorization, etc. |
| Complex Numbers | 8 | four operations, magnitude, conjugate, polar form |
| Matrices | 7 | matrix ops, determinant, inverse, vector ops |
| Numerical Analysis | 16 | integration, differentiation, root finding, interpolation |
| Financial | 7 | compound interest, annuities, loans, NPV, IRR, bonds |
| Conversions | 5 | length, weight, temperature, area, time |
| Geometry | 6 | plane, solid, coordinate geometry |

### Error types

| Error type | Trigger | Example |
|----------|----------|------|
| Division by zero | divisor is 0 | `divide(10, 0)` |
| Math domain error | even root of a negative | `sqrt(-4)` |
| Range error | inverse trig input outside [-1,1] | `asin(2)` |
| Argument error | non-positive log input | `ln(-1)` |

### Return format

All tool calls return a consistent format:

```typescript
interface ToolResult {
  content: [{
    type: "text";
    text: string;
  }];
  isError?: boolean;
}
```

**Official site: ** [https://github.com/proflulab/mcp-calculator.git](https://github.com/proflulab/mcp-calculator.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `other`, `developer tools`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-calculator`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/shimingy-calculator.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
