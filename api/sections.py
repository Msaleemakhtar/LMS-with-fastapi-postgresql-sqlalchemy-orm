import fastapi


router = fastapi.APIRouter()


@router.get("/sections/{id}")
async def read_section():
    return {"course; ": []}


@router.get("/section/{id}/content_blocks")
async def read_section_content_block():
    return {"course; ": []}


@router.get("/content_blocks/{id}")
async def read_content_block():
    return {"course; ": []}
