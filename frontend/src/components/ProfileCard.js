class ProfileCard {
    constructor() {
        this.avatarUrl = 'https://ai-public.mastergo.com/ai/img_res/766ae7e3422e069abe169b013eb46649.jpg';
        this.nickname = '';
        this.location = '';
        this.profession = '';
        this.workYears = 0;
        this.advantages = [
            '拥有出境旅行社，专注俄罗斯及新加坡目的地接待，可承接旅游、商务、展会等多样化需求',
            '8年互联网产品海外流量投放经验，覆盖社交、教育、工具、汽车等领域',
            '深耕汽车行业资源，拥有丰富的汽车媒体渠道合作经验'
        ];
        this.tags = ['出境旅游', '俄罗斯地接', '新加坡游学', '海外营销', '流量投放', '汽车行业', 'Google投放', 'Facebook投放'];
        this.templates = [
            { preview: 'https://ai-public.mastergo.com/ai/img_res/3b2b2012a1dd90d2936abb3bbd10b9bd.jpg' },
            { preview: 'https://ai-public.mastergo.com/ai/img_res/b62417e6e106a18057a67e80b7ba877d.jpg' },
            { preview: 'https://ai-public.mastergo.com/ai/img_res/9e801029ab32866ecf6c73d5c83e7e4f.jpg' }
        ];
        this.currentTemplate = 0;
    }

    generateHTML() {
        return `
            <div class="bg-white rounded-xl shadow-sm">
                <!-- 头像和基础信息 -->
                <div class="p-6">
                    <div class="flex items-start mb-6">
                        <div class="relative w-20 h-20">
                            <img src="${this.avatarUrl}" class="w-full h-full rounded-full object-cover shadow-md" alt="头像" />
                        </div>
                        <div class="ml-4 flex-1">
                            <div class="text-xl font-medium mb-1">${this.nickname || 'Fendy'}</div>
                            <div class="flex items-center text-sm text-gray-600">
                                <i class="fas fa-map-marker-alt mr-1"></i>
                                <span>${this.location || '北京朝阳'}</span>
                            </div>
                        </div>
                    </div>

                    <div class="space-y-4">
                        <div class="flex items-center">
                            <i class="fas fa-briefcase text-blue-500 w-6"></i>
                            <span class="text-sm">${this.profession || '汽车之家内容运营 / 私人订制旅行社老板'}</span>
                        </div>
                        
                        <div class="flex items-center">
                            <i class="fas fa-clock text-blue-500 w-6"></i>
                            <span class="text-sm text-gray-600">从业年限</span>
                            <span class="text-sm text-gray-600 ml-2">${this.workYears}年</span>
                        </div>
                    </div>
                </div>

                <!-- 核心优势 -->
                <div class="p-6 border-t">
                    <h3 class="text-base font-medium mb-4 flex items-center">
                        <i class="fas fa-star text-yellow-400 mr-2"></i>
                        核心优势
                    </h3>
                    <div class="space-y-3">
                        ${this.advantages.map(advantage => `
                            <div class="flex items-start p-3 rounded-lg bg-blue-50">
                                <i class="fas fa-check-circle text-blue-500 mt-1"></i>
                                <p class="ml-3 text-sm text-gray-700">${advantage}</p>
                            </div>
                        `).join('')}
                    </div>
                </div>

                <!-- 技能标签 -->
                <div class="p-6 border-t">
                    <h3 class="text-base font-medium mb-4">专业技能</h3>
                    <div class="flex flex-wrap gap-2">
                        ${this.tags.map(tag => `
                            <div class="px-4 py-2 bg-gradient-to-r from-blue-50 to-blue-100 rounded-full text-sm text-blue-600">
                                ${tag}
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        `;
    }

    // 将 HTML 转换为图片
    async generateImage() {
        const html = this.generateHTML();
        // 这里需要使用 html2canvas 或其他库将 HTML 转换为图片
        // 为了演示，我们先返回一个示例图片
        return this.templates[this.currentTemplate].preview;
    }

    // 更新数据
    updateData(data) {
        Object.assign(this, data);
    }
}

export default ProfileCard;
