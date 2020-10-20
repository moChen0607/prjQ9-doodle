#pragma once

#include "Widgets/SCompoundWidget.h"
#include "Widgets/DeclarativeSyntaxSupport.h"
#include "UObject/GCObject.h"

class DoodleCopyMat :public SCompoundWidget, public FGCObject
{
public:
    SLATE_BEGIN_ARGS(DoodleCopyMat) {}
    SLATE_END_ARGS( )
    //���������ݴ�������
    void Construct(const FArguments& Arg);
    //�����ʱ��֪��ʲô��˼,���ǲ��Ӿͼ��ѱ��벻��ȥ
    virtual void AddReferencedObjects(FReferenceCollector& collector) override;

private:
    FReply getSelect( );
    FReply CopyMateral( );

private:
    USkeletalMesh* copySoure;
};