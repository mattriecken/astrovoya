import { useEffect, useRef } from "react";

const AladinMap = () => {
    const aladinRef = useRef(null);

    useEffect(() => {
        if (!window.A) return;

        const aladin = window.A.aladin(aladinRef.current, {
            survey: 'P/DSS2/color',
            fov: 180,
            projection: 'AIT',
            showControl: true,
            showFullscreenControl: true,
            showZoomControl: true,
        });

        aladin.gotoRaDec(180, 45);

    }, []);

    return (
        <div
            ref={aladinRef}
            style={{ width: '100%', height: '100vh' }}
        />
    );
};

export default AladinMap;