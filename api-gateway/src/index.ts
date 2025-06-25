import express, { NextFunction, Request, Response } from "express";
import dotenv from "dotenv";
import cors from "cors";
import { logger } from "./utils/logger";
import { verifyJWT } from "./middleware/authMiddleware";
import { apiRateLimiter } from "./middleware/rateLimiter";
import routes from "./routes/routes";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());
app.use(logger);
app.use(apiRateLimiter);
// app.use(verifyJWT);

app.use(routes);

app.get("/health", (req: Request, res: Response) => {
    res.status(200).json({ status: "API Gateway healthy" });
});

app.use((err: any, req: Request, res: Response, next: NextFunction) => {
    console.error("Gateway Error:", err.message);
    res.status(500).json({ error: "Internal Server Error" });
});

app.listen(8080, () =>
    console.log(`🚪 API Gateway running on http://localhost:${PORT}`)
);
