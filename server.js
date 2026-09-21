import express from 'express'
import { existsSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const app = express()
const port = Number(process.env.PORT) || 3000
const host = '0.0.0.0'
const rootDir = path.dirname(fileURLToPath(import.meta.url))
const distDir = path.join(rootDir, 'dist')
const indexFile = path.join(distDir, 'index.html')

if (!existsSync(indexFile)) {
  console.error('Production build not found. Run "npm run build" before "npm start".')
  process.exit(1)
}

app.disable('x-powered-by')
app.use(express.static(distDir, { extensions: ['html'] }))

// The portfolio uses anchor navigation, but this fallback also keeps future
// client-side routes from returning a server 404. Middleware is compatible
// with Express 5's stricter route pattern parser.
app.use((_request, response) => response.sendFile(indexFile))

app.listen(port, host, () => {
  console.log(`Server running on http://${host}:${port}`)
})
