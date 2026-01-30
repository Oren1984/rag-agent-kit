# scripts/audit.ps1
# Basic audit script for RAG setup

Write-Host "RAG AUDIT (basic)..." -ForegroundColor Cyan

# Check for .env file and required variables
$envFile = ".\.env"
if (-not (Test-Path $envFile)) { Write-Host "FAIL: .env missing" -ForegroundColor Red; exit 1 }

# Read .env file
$envText = Get-Content $envFile -Raw

# Check for required variables
if ($envText -notmatch "RAG_API_KEY=") { Write-Host "FAIL: RAG_API_KEY missing" -ForegroundColor Red; exit 1 }
if ($envText -match "WEB_SEARCH_ENABLED=true") { Write-Host "WARN: Web search enabled" -ForegroundColor Yellow }

# Check for required directories
Write-Host "PASS: basic checks ok" -ForegroundColor Green
