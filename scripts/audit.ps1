Write-Host "RAG AUDIT (basic)..." -ForegroundColor Cyan

$envFile = ".\.env"
if (-not (Test-Path $envFile)) { Write-Host "FAIL: .env missing" -ForegroundColor Red; exit 1 }

$envText = Get-Content $envFile -Raw

if ($envText -notmatch "RAG_API_KEY=") { Write-Host "FAIL: RAG_API_KEY missing" -ForegroundColor Red; exit 1 }
if ($envText -match "WEB_SEARCH_ENABLED=true") { Write-Host "WARN: Web search enabled" -ForegroundColor Yellow }

Write-Host "PASS: basic checks ok" -ForegroundColor Green
