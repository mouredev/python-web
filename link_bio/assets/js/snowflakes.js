import { useEffect } from 'react';

export function Snowflakes() {

    useEffect(() => {
        function handlePageChange() {
            clearSnowflakes();
            generateSnowflakes();
        }

        function clearSnowflakes() {
            const snowflakes = document.querySelectorAll(".snowflake");
            snowflakes.forEach(snowflake => snowflake.remove());
        }

        function getSupportedPropertyName(properties) {
            for (var i = 0; i < properties.length; i++) {
                if (typeof document.body.style[properties[i]] !== "undefined") {
                    return properties[i];
                }
            }
            return null;
        }

        class Snowflake {
            constructor(element, speed, xPos, yPos) {
                this.element = element;
                this.speed = speed;
                this.xPos = xPos;
                this.yPos = yPos;
                this.counter = 0;
                this.sign = Math.random() < 0.5 ? 1 : -1;
                this.element.style.opacity = 0.1 + Math.random();
                this.element.style.fontSize = 12 + 50 * Math.random() + 'px';
            }

            update() {
                this.counter += this.speed / 5000;
                this.xPos += this.sign * this.speed * Math.cos(this.counter) / 40;
                this.yPos += Math.sin(this.counter) / 40 + this.speed / 30;
                setTranslate3DTransform(this.element, Math.round(this.xPos), Math.round(this.yPos));

                if (this.yPos > browserHeight) {
                    this.yPos = -50;
                }
            }
        }

        function setTranslate3DTransform(element, x, y) {
            var transform = "translate3d(" + x + "px, " + y + "px, 0)";
            element.style[transformProperty] = transform;
        }

        function generateSnowflakes() {
            var originalSnowflake = document.querySelector(".snowflake");
            if (!originalSnowflake) {
                console.error("No element with class 'snowflake' found");
                return;
            }
            var container = originalSnowflake.parentNode;
            browserWidth = document.documentElement.clientWidth;
            browserHeight = document.documentElement.clientHeight;

            for (var i = 0; i < numberOfSnowflakes; i++) {
                var clone = originalSnowflake.cloneNode(true);
                container.appendChild(clone);
                var xPos = getPosition(50, browserWidth);
                var yPos = getPosition(50, browserHeight);
                var speed = 5 + 40 * Math.random();
                var snowflake = new Snowflake(clone, speed, xPos, yPos);
                snowflakes.push(snowflake);
            }
            container.removeChild(originalSnowflake);
            moveSnowflakes();
        }

        function moveSnowflakes() {
            for (var i = 0; i < snowflakes.length; i++) {
                var snowflake = snowflakes[i];
                snowflake.update();
            }
            if (resetPosition) {
                browserWidth = document.documentElement.clientWidth;
                browserHeight = document.documentElement.clientHeight;
                for (var i = 0; i < snowflakes.length; i++) {
                    var snowflake = snowflakes[i];
                    snowflake.xPos = getPosition(50, browserWidth);
                    snowflake.yPos = getPosition(50, browserHeight);
                }
                resetPosition = false;
            }
            requestAnimationFrame(moveSnowflakes);
        }

        function getPosition(offset, size) {
            return Math.round(-1 * offset + Math.random() * (size + 2 * offset));
        }

        function setResetFlag() {
            resetPosition = true;
        }

        var requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;
        var transforms = ["transform", "msTransform", "webkitTransform", "mozTransform", "oTransform"];
        var transformProperty = getSupportedPropertyName(transforms);
        var snowflakes = [];
        var browserWidth;
        var browserHeight;
        var numberOfSnowflakes = 25;
        var resetPosition = false;

        generateSnowflakes();
        window.addEventListener("resize", setResetFlag, false);
        window.addEventListener("popstate", handlePageChange, false);

        return () => {
            window.removeEventListener("resize", setResetFlag, false);
            window.removeEventListener("popstate", handlePageChange, false);
        };
    }, []);

    return null;
}