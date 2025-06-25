import express from "express";
import { createProxyMiddleware } from "http-proxy-middleware";
import dotenv from "dotenv";
dotenv.config();
const router = express.Router();

router.use(
    "/api/v1/auth",
    createProxyMiddleware({
        target: process.env.AUTH_SERVICE,
        changeOrigin: true,
        pathRewrite: { "^/api/v1/auth": "" },
        logger: console,
    })
);

router.use(
    "/api/v1/products",
    createProxyMiddleware({
        target: `${process.env.PRODUCT_SERVICE}/products`,
        changeOrigin: true,
        // pathRewrite: { "^/api/v1": "" },
        logger: console,
    })
);

export default router;
