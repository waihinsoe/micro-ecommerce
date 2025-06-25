import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

// Allow unauthenticated access to auth service
const isPublicRoute = (path: string) => path.startsWith("/api/v1/auth");

export const verifyJWT = (req: Request, res: Response, next: NextFunction) => {
    if (isPublicRoute(req.path)) return next();

    const authHeader = req.headers["authorization"];
    const token = authHeader && authHeader.split(" ")[1];

    if (!token) {
        res.status(401).json({ error: "No token provided" });
        return;
    }

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET as string);
        (req as any).user = decoded; // You can forward this in headers if needed
        next();
    } catch (err) {
        res.status(403).json({ error: "Invalid token" });
    }
};
