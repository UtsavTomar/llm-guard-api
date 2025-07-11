# Deploying LLM Guard API to Vercel

This guide will help you deploy the LLM Guard API to Vercel.

## Prerequisites

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Make sure you have a Vercel account at [vercel.com](https://vercel.com)

## Deployment Steps

### 1. Login to Vercel
```bash
vercel login
```

### 2. Deploy the Application
From the project root directory, run:
```bash
vercel
```

Follow the prompts:
- Set up and deploy? `Y`
- Which scope? Select your account
- Link to existing project? `N`
- What's your project's name? `llm-guard-api` (or your preferred name)
- In which directory is your code located? `./` (current directory)

### 3. Environment Variables (Optional)
You can set environment variables in the Vercel dashboard or via CLI:

```bash
vercel env add CONFIG_FILE
vercel env add APP_NAME
vercel env add LOG_LEVEL
vercel env add AUTH_TOKEN
```

### 4. Production Deployment
To deploy to production:
```bash
vercel --prod
```

## Configuration

The application uses the `config/scanners.yml` file for configuration. You can customize this file to enable/disable specific scanners or modify their parameters.

### Important Notes

1. **Cold Starts**: The first request to your API might be slower due to cold starts, especially with the ML models used by LLM Guard.

2. **Function Timeout**: The function timeout is set to 30 seconds in `vercel.json`. You may need to adjust this based on your needs.

3. **Memory Usage**: LLM Guard uses ML models which can be memory-intensive. Monitor your function's memory usage in the Vercel dashboard.

4. **API Authentication**: The default configuration uses HTTP Bearer token authentication. Make sure to set a secure token in production.

## API Endpoints

Once deployed, your API will be available at:
- `https://your-project-name.vercel.app/`

Available endpoints:
- `GET /` - Health check
- `GET /healthz` - Health check
- `GET /readyz` - Readiness check
- `POST /analyze/prompt` - Analyze and sanitize prompts
- `POST /scan/prompt` - Scan prompts without sanitization
- `POST /analyze/output` - Analyze and sanitize outputs
- `POST /scan/output` - Scan outputs without sanitization
- `GET /metrics` - Prometheus metrics (if enabled)

## Troubleshooting

1. **Import Errors**: Make sure all dependencies are listed in `requirements.txt`
2. **Timeout Issues**: Increase the `maxDuration` in `vercel.json`
3. **Memory Issues**: Consider using fewer scanners or optimizing the configuration
4. **Authentication Issues**: Check your auth configuration in `config/scanners.yml`

## Local Development

To test locally before deploying:
```bash
pip install -r requirements.txt
python api/index.py
```

The API will be available at `http://localhost:8000` 